#!/usr/bin/env ts-node
"use strict";
/**
 * Kaitiaki Aronui Memory System - The Hippocampus of Te Kete Ako
 *
 * This is the episodic memory system that catalogs and indexes every artifact
 * created by our AI agents. It's like having a photographic memory of everything
 * that's been built for Mangakōtukutuku College.
 *
 * The system learns from patterns: which resources work, what teachers modify,
 * how students respond. This becomes the foundation for increasingly intelligent
 * content generation.
 */
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g = Object.create((typeof Iterator === "function" ? Iterator : Object).prototype);
    return g.next = verb(0), g["throw"] = verb(1), g["return"] = verb(2), typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (g && (g = 0, op[0] && (_ = 0)), _) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
var __spreadArray = (this && this.__spreadArray) || function (to, from, pack) {
    if (pack || arguments.length === 2) for (var i = 0, l = from.length, ar; i < l; i++) {
        if (ar || !(i in from)) {
            if (!ar) ar = Array.prototype.slice.call(from, 0, i);
            ar[i] = from[i];
        }
    }
    return to.concat(ar || Array.prototype.slice.call(from));
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.indexTeKeteAko = indexTeKeteAko;
exports.processArtifact = processArtifact;
var fs = require("fs");
var path = require("path");
var crypto = require("crypto");
var fg = require("fast-glob");
var pdfParse = require("pdf-parse");
var cheerio = require("cheerio");
var front_matter_1 = require("front-matter");
var supabase_js_1 = require("@supabase/supabase-js");
var axios_1 = require("axios");
var dotenv = require("dotenv");
dotenv.config();
// Configuration - The nervous system of our indexer
var config = {
    supabase: {
        url: process.env.SUPABASE_URL,
        key: process.env.SUPABASE_SERVICE_KEY
    },
    ai: {
        deepseekKey: process.env.DEEPSEEK_API_KEY || 'sk-103cb83572a346e2aef89e2d2a4f7f89',
        openaiKey: process.env.OPENAI_API_KEY || '',
        embeddingModel: 'text-embedding-3-large',
        embeddingDim: 1536
    },
    patterns: [
        '**/*.md', '**/*.markdown', '**/*.html', '**/*.htm',
        '**/*.pdf', '**/*.txt', '**/*.json', '**/*.py', '**/*.js', '**/*.ts'
    ],
    cultural: {
        maoriWords: ['māori', 'iwi', 'hapū', 'whānau', 'kaiako', 'ākonga', 'kōrero', 'whakatōhea', 'manaakitanga', 'ako'],
        culturalConcepts: ['te ao māori', 'tikanga', 'kaupapa', 'whakapapa', 'taonga', 'mauri']
    }
};
if (!config.supabase.url || !config.supabase.key) {
    console.error('❌ Missing Supabase credentials. Set SUPABASE_URL and SUPABASE_SERVICE_KEY');
    process.exit(1);
}
var supabase = (0, supabase_js_1.createClient)(config.supabase.url, config.supabase.key);
// ========================================
// MEMORY ENCODING FUNCTIONS
// ========================================
function sha256(content) {
    return crypto.createHash('sha256').update(content).digest('hex');
}
function embedWithOpenAI(text) {
    return __awaiter(this, void 0, void 0, function () {
        var response, error_1;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    if (!config.ai.openaiKey) {
                        console.warn('⚠️  No OpenAI key - using random vector (NOT for production)');
                        return [2 /*return*/, Array.from({ length: config.ai.embeddingDim }, function () { return Math.random() - 0.5; })];
                    }
                    _a.label = 1;
                case 1:
                    _a.trys.push([1, 3, , 4]);
                    return [4 /*yield*/, axios_1.default.post('https://api.openai.com/v1/embeddings', {
                            model: config.ai.embeddingModel,
                            input: text.slice(0, 8000) // Truncate for API limits
                        }, {
                            headers: { Authorization: "Bearer ".concat(config.ai.openaiKey) }
                        })];
                case 2:
                    response = _a.sent();
                    return [2 /*return*/, response.data.data[0].embedding];
                case 3:
                    error_1 = _a.sent();
                    console.warn('⚠️  Embedding failed, using random vector:', error_1);
                    return [2 /*return*/, Array.from({ length: config.ai.embeddingDim }, function () { return Math.random() - 0.5; })];
                case 4: return [2 /*return*/];
            }
        });
    });
}
function extractCulturalContext(text) {
    var lowerText = text.toLowerCase();
    var foundWords = config.cultural.maoriWords.filter(function (word) { return lowerText.includes(word); });
    var foundConcepts = config.cultural.culturalConcepts.filter(function (concept) { return lowerText.includes(concept); });
    var tags = __spreadArray(__spreadArray([], foundWords, true), foundConcepts, true);
    var significance = tags.length > 0 ? 'Contains Māori cultural elements' : 'General educational content';
    return { tags: Array.from(new Set(tags)), significance: significance };
}
function extractKeywords(text, maxKeywords) {
    if (maxKeywords === void 0) { maxKeywords = 10; }
    if (!text)
        return [];
    // Simple keyword extraction - focuses on educational terms
    var words = text
        .toLowerCase()
        .replace(/[^\w\s]/g, ' ')
        .split(/\s+/)
        .filter(function (word) {
        return word.length > 3 &&
            !['this', 'that', 'with', 'have', 'will', 'been', 'from', 'they', 'were', 'said', 'each', 'which', 'your', 'what', 'their', 'time', 'about'].includes(word);
    });
    var frequency = {};
    words.forEach(function (word) { return frequency[word] = (frequency[word] || 0) + 1; });
    return Object.entries(frequency)
        .sort(function (_a, _b) {
        var a = _a[1];
        var b = _b[1];
        return b - a;
    })
        .slice(0, maxKeywords)
        .map(function (_a) {
        var word = _a[0];
        return word;
    });
}
// ========================================
// CONTENT EXTRACTORS
// ========================================
function extractFromPDF(buffer) {
    return __awaiter(this, void 0, void 0, function () {
        var data, text, title, error_2;
        var _a;
        return __generator(this, function (_b) {
            switch (_b.label) {
                case 0:
                    _b.trys.push([0, 2, , 3]);
                    return [4 /*yield*/, pdfParse(buffer)];
                case 1:
                    data = _b.sent();
                    text = data.text || '';
                    title = ((_a = text.split('\n').find(function (line) { return line.trim().length > 0; })) === null || _a === void 0 ? void 0 : _a.slice(0, 100)) || 'Untitled PDF';
                    return [2 /*return*/, { text: text, title: title }];
                case 2:
                    error_2 = _b.sent();
                    console.warn('PDF parsing failed:', error_2);
                    return [2 /*return*/, { text: '', title: 'PDF (parsing failed)' }];
                case 3: return [2 /*return*/];
            }
        });
    });
}
function extractFromHTML(html) {
    try {
        var $_1 = cheerio.load(html);
        var title = $_1('title').text() || $_1('h1').first().text() || 'Untitled HTML';
        var headings_1 = [];
        $_1('h1, h2, h3, h4').each(function (_, elem) {
            var heading = $_1(elem).text().trim();
            if (heading)
                headings_1.push(heading);
        });
        var text = $_1('body').text().replace(/\s+/g, ' ').trim();
        return { text: text, title: title, headings: headings_1 };
    }
    catch (error) {
        console.warn('HTML parsing failed:', error);
        return { text: html, title: 'HTML (parsing failed)', headings: [] };
    }
}
function extractFromMarkdown(content) {
    var _a;
    try {
        var parsed = (0, front_matter_1.default)(content);
        var metadata = parsed.attributes || {};
        var text = String(parsed.body || content);
        var title = metadata.title || ((_a = text.split('\n').find(function (line) { return line.startsWith('#'); })) === null || _a === void 0 ? void 0 : _a.replace(/^#+\s*/, '')) || 'Untitled';
        return { text: text, title: title, metadata: metadata };
    }
    catch (error) {
        return { text: content, title: 'Markdown (parsing failed)', metadata: {} };
    }
}
// ========================================
// ARTIFACT PROCESSING
// ========================================
function processArtifact(filePath, rootDir) {
    return __awaiter(this, void 0, void 0, function () {
        var relPath_1, ext_1, stat, buffer, contentHash, existing, title, description, keywords, yearLevels, subjects, metadata, agent_creator, _a, text, pdfTitle, _b, text, htmlTitle, headings, _c, text, mdTitle, mdMeta, code, firstComment, text, parseError_1, fullText, _d, culturalTags, significance, embedding, fileType, qualityScore, artifact, error, error_3;
        var _e, _f, _g;
        return __generator(this, function (_h) {
            switch (_h.label) {
                case 0:
                    _h.trys.push([0, 10, , 11]);
                    relPath_1 = path.relative(rootDir, filePath);
                    ext_1 = path.extname(filePath).toLowerCase();
                    stat = fs.statSync(filePath);
                    buffer = fs.readFileSync(filePath);
                    contentHash = sha256(buffer);
                    return [4 /*yield*/, supabase
                            .from('artifact_catalog')
                            .select('content_hash')
                            .eq('file_path', relPath_1)
                            .single()];
                case 1:
                    existing = (_h.sent()).data;
                    if ((existing === null || existing === void 0 ? void 0 : existing.content_hash) === contentHash) {
                        console.log("\u23ED\uFE0F  Skipping ".concat(relPath_1, " (unchanged)"));
                        return [2 /*return*/];
                    }
                    title = path.basename(filePath, ext_1);
                    description = '';
                    keywords = [];
                    yearLevels = [];
                    subjects = [];
                    metadata = {};
                    agent_creator = 'unknown';
                    _h.label = 2;
                case 2:
                    _h.trys.push([2, 6, , 7]);
                    if (!(ext_1 === '.pdf')) return [3 /*break*/, 4];
                    return [4 /*yield*/, extractFromPDF(buffer)];
                case 3:
                    _a = _h.sent(), text = _a.text, pdfTitle = _a.title;
                    title = pdfTitle;
                    description = text.slice(0, 500).replace(/\s+/g, ' ').trim() + (text.length > 500 ? '...' : '');
                    keywords = extractKeywords(text);
                    return [3 /*break*/, 5];
                case 4:
                    if (['.html', '.htm'].includes(ext_1)) {
                        _b = extractFromHTML(buffer.toString('utf8')), text = _b.text, htmlTitle = _b.title, headings = _b.headings;
                        title = htmlTitle;
                        description = text.slice(0, 500).replace(/\s+/g, ' ').trim() + (text.length > 500 ? '...' : '');
                        keywords = extractKeywords(__spreadArray(__spreadArray([], headings, true), [text], false).join(' '));
                    }
                    else if (['.md', '.markdown'].includes(ext_1)) {
                        _c = extractFromMarkdown(buffer.toString('utf8')), text = _c.text, mdTitle = _c.title, mdMeta = _c.metadata;
                        title = mdTitle;
                        description = mdMeta.description || text.slice(0, 500).replace(/\s+/g, ' ').trim() + (text.length > 500 ? '...' : '');
                        keywords = mdMeta.tags || extractKeywords(text);
                        yearLevels = mdMeta.year_levels || mdMeta.yearLevels || [];
                        subjects = mdMeta.subjects || [];
                        metadata = mdMeta;
                        agent_creator = mdMeta.agent || mdMeta.created_by || 'unknown';
                    }
                    else if (['.js', '.ts', '.py'].includes(ext_1)) {
                        code = buffer.toString('utf8');
                        firstComment = code.match(/\/\*\*([\s\S]*?)\*\/|"""([\s\S]*?)"""|'''([\s\S]*?)'''/);
                        title = firstComment ? ((_f = (_e = firstComment[1]) === null || _e === void 0 ? void 0 : _e.split('\n')[0]) === null || _f === void 0 ? void 0 : _f.trim()) || title : title;
                        description = "Code file: ".concat(ext_1.slice(1), " script");
                        keywords = extractKeywords(code);
                    }
                    else {
                        text = buffer.toString('utf8');
                        description = text.slice(0, 500).replace(/\s+/g, ' ').trim() + (text.length > 500 ? '...' : '');
                        keywords = extractKeywords(text);
                    }
                    _h.label = 5;
                case 5: return [3 /*break*/, 7];
                case 6:
                    parseError_1 = _h.sent();
                    console.warn("\u26A0\uFE0F  Parse error for ".concat(relPath_1, ":"), parseError_1);
                    description = "File processing error: ".concat(parseError_1);
                    return [3 /*break*/, 7];
                case 7:
                    fullText = [title, description, keywords.join(' ')].join(' ');
                    _d = extractCulturalContext(fullText), culturalTags = _d.tags, significance = _d.significance;
                    return [4 /*yield*/, embedWithOpenAI(fullText)];
                case 8:
                    embedding = _h.sent();
                    fileType = 'unknown';
                    if (['lesson', 'unit', 'handout', 'activity', 'game'].some(function (t) { return relPath_1.toLowerCase().includes(t); })) {
                        fileType = 'educational_resource';
                    }
                    else if (['script', 'py', 'js', 'ts'].some(function (t) { return relPath_1.toLowerCase().includes(t) || ext_1 === ".".concat(t); })) {
                        fileType = 'script';
                    }
                    else if (['doc', 'md', 'readme', 'guide'].some(function (t) { return relPath_1.toLowerCase().includes(t); })) {
                        fileType = 'documentation';
                    }
                    else if (ext_1 === '.pdf') {
                        fileType = 'pdf_resource';
                    }
                    qualityScore = 0.5;
                    if (title && title !== path.basename(filePath, ext_1))
                        qualityScore += 0.2; // has meaningful title
                    if (description.length > 100)
                        qualityScore += 0.2; // substantial description
                    if (keywords.length >= 3)
                        qualityScore += 0.1; // good keywords
                    if (culturalTags.length > 0)
                        qualityScore += 0.2; // cultural integration
                    qualityScore = Math.min(1.0, qualityScore);
                    artifact = {
                        file_path: relPath_1,
                        file_name: path.basename(filePath),
                        file_type: fileType,
                        file_size_bytes: stat.size,
                        content_hash: contentHash,
                        title: title.slice(0, 300),
                        description: description.slice(0, 1000),
                        keywords: keywords,
                        year_levels: yearLevels,
                        subjects: subjects,
                        cultural_tags: culturalTags,
                        agent_creator: agent_creator,
                        quality_score: qualityScore,
                        embedding: embedding,
                        metadata: metadata,
                        created_at: ((_g = stat.birthtime) === null || _g === void 0 ? void 0 : _g.toISOString()) || new Date().toISOString(),
                        updated_at: new Date().toISOString()
                    };
                    return [4 /*yield*/, supabase
                            .from('artifact_catalog')
                            .upsert(artifact, { onConflict: 'file_path' })];
                case 9:
                    error = (_h.sent()).error;
                    if (error)
                        throw error;
                    console.log("\u2705 Indexed: ".concat(relPath_1, " (").concat(fileType, ", quality: ").concat(qualityScore.toFixed(2), ")"));
                    return [3 /*break*/, 11];
                case 10:
                    error_3 = _h.sent();
                    console.error("\u274C Failed to process ".concat(filePath, ":"), error_3);
                    return [3 /*break*/, 11];
                case 11: return [2 /*return*/];
            }
        });
    });
}
// ========================================
// MAIN INDEXING FUNCTION
// ========================================
function indexTeKeteAko(rootDir) {
    return __awaiter(this, void 0, void 0, function () {
        var files, processed, _i, files_1, file, stats, summary, error_4;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    console.log('🧠 Kaitiaki Aronui Memory System - Indexing Te Kete Ako');
                    console.log('📁 Scanning directory:', rootDir);
                    _a.label = 1;
                case 1:
                    _a.trys.push([1, 8, , 9]);
                    return [4 /*yield*/, fg(config.patterns, {
                            cwd: rootDir,
                            absolute: true,
                            dot: true,
                            ignore: ['**/node_modules/**', '**/.*/**', '**/*.log', '**/backups/**']
                        })];
                case 2:
                    files = _a.sent();
                    console.log("\uD83D\uDCCA Found ".concat(files.length, " artifacts to catalog"));
                    processed = 0;
                    _i = 0, files_1 = files;
                    _a.label = 3;
                case 3:
                    if (!(_i < files_1.length)) return [3 /*break*/, 6];
                    file = files_1[_i];
                    return [4 /*yield*/, processArtifact(file, rootDir)];
                case 4:
                    _a.sent();
                    processed++;
                    if (processed % 10 === 0) {
                        console.log("\uD83D\uDCC8 Progress: ".concat(processed, "/").concat(files.length, " (").concat(Math.round(processed / files.length * 100), "%)"));
                    }
                    _a.label = 5;
                case 5:
                    _i++;
                    return [3 /*break*/, 3];
                case 6: return [4 /*yield*/, supabase
                        .from('artifact_catalog')
                        .select('file_type')];
                case 7:
                    stats = (_a.sent()).data;
                    console.log('\n🎯 Indexing Complete!');
                    console.log('📊 Summary:');
                    if (stats && Array.isArray(stats)) {
                        summary = stats.reduce(function (acc, item) {
                            acc[item.file_type] = (acc[item.file_type] || 0) + 1;
                            return acc;
                        }, {});
                        Object.entries(summary).forEach(function (_a) {
                            var fileType = _a[0], count = _a[1];
                            console.log("   ".concat(fileType, ": ").concat(count, " artifacts"));
                        });
                    }
                    console.log('\n🧺 "Whaowhia te kete mātauranga" - The basket of knowledge is now indexed!');
                    return [3 /*break*/, 9];
                case 8:
                    error_4 = _a.sent();
                    console.error('❌ Indexing failed:', error_4);
                    throw error_4;
                case 9: return [2 /*return*/];
            }
        });
    });
}
// ========================================
// CLI INTERFACE
// ========================================
function main() {
    return __awaiter(this, void 0, void 0, function () {
        var targetDir, resolvedDir, error_5;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    targetDir = process.argv[2] || './te-kete-ako-clean';
                    resolvedDir = path.resolve(targetDir);
                    if (!fs.existsSync(resolvedDir)) {
                        console.error("\u274C Directory not found: ".concat(resolvedDir));
                        process.exit(1);
                    }
                    console.log("\uD83D\uDE80 Starting memory indexing for: ".concat(resolvedDir));
                    _a.label = 1;
                case 1:
                    _a.trys.push([1, 3, , 4]);
                    return [4 /*yield*/, indexTeKeteAko(resolvedDir)];
                case 2:
                    _a.sent();
                    console.log('✨ Memory indexing completed successfully!');
                    return [3 /*break*/, 4];
                case 3:
                    error_5 = _a.sent();
                    console.error('💥 Memory indexing failed:', error_5);
                    process.exit(1);
                    return [3 /*break*/, 4];
                case 4: return [2 /*return*/];
            }
        });
    });
}
// Run if called directly
if (require.main === module) {
    main();
}
