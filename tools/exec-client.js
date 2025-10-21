#!/usr/bin/env node

const http = require('http');

function request(method, path, payload) {
    return new Promise((resolve, reject) => {
        const data = payload ? Buffer.from(JSON.stringify(payload)) : null;
        const req = http.request({
            hostname: '127.0.0.1',
            port: 3002,
            path,
            method,
            headers: {
                'Content-Type': 'application/json',
                'Content-Length': data ? data.length : 0
            }
        }, (res) => {
            let body = '';
            res.on('data', (chunk) => body += chunk.toString());
            res.on('end', () => {
                try { resolve(JSON.parse(body || '{}')); }
                catch { resolve({ raw: body }); }
            });
        });
        req.on('error', reject);
        if (data) req.write(data);
        req.end();
    });
}

async function main() {
    const [,, action = 'caps', command = 'npm', ...args] = process.argv;
    if (action === 'caps') {
        const caps = await request('GET', '/exec/capabilities');
        console.log(JSON.stringify(caps, null, 2));
        return;
    }
    if (action === 'run') {
        const payload = {
            agentId: 'agent-cli',
            command,
            args,
            dryRun: process.env.DRY_RUN === '1',
            timeoutMs: process.env.TIMEOUT_MS ? parseInt(process.env.TIMEOUT_MS, 10) : undefined,
            workingDir: process.env.WORKING_DIR || ''
        };
        const res = await request('POST', '/exec', payload);
        console.log(JSON.stringify(res, null, 2));
        return;
    }
    console.log('Usage:\n  exec-client.js caps\n  exec-client.js run <command> [args...]\n  DRY_RUN=1 exec-client.js run npm -v');
}

main().catch((e) => {
    console.error(e);
    process.exit(1);
});
