import{j as e,r as a}from"./main-BpcvedNI.js";const c=({problems:n})=>{const i=Math.ceil(n.length/2),l=n.slice(0,i),o=n.slice(i,n.length);return e.jsxDEV("div",{className:"printable-a4-horizontal",children:[e.jsxDEV("style",{children:`
          @media print {
            @page {
              size: A4 landscape;
              margin: 1cm;
            }
            body * {
              visibility: hidden;
            }
            .printable-a4-horizontal, .printable-a4-horizontal * {
              visibility: visible;
            }
            .printable-a4-horizontal {
              position: absolute;
              left: 0;
              top: 0;
              width: 100%;
            }
          }
          .printable-a4-horizontal {
            width: 297mm;
            height: 210mm;
            display: flex;
            flex-direction: row;
            border: 1px solid #ccc;
            margin: 20px auto;
            padding: 10mm;
            background: white;
          }
          .quiz-section {
            width: 50%;
            height: 100%;
            padding: 0 5mm;
            display: flex;
            flex-direction: column;
          }
          .quiz-section:first-child {
            border-right: 1px dashed #ccc;
          }
          .quiz-header {
            text-align: center;
            margin-bottom: 10px;
          }
          .problem-list {
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 15px 5px;
          }
          .problem-item {
            font-size: 14px;
          }
        `},void 0,!1,{fileName:"/Users/admin/Documents/te-kete-ako-clean/src/components/PrintableWorksheet.tsx",lineNumber:19,columnNumber:7},void 0),e.jsxDEV("div",{className:"quiz-section",children:[e.jsxDEV("div",{className:"quiz-header",children:[e.jsxDEV("h3",{children:"Addition Practice"},void 0,!1,{fileName:"/Users/admin/Documents/te-kete-ako-clean/src/components/PrintableWorksheet.tsx",lineNumber:75,columnNumber:11},void 0),e.jsxDEV("p",{children:"Name: _______________"},void 0,!1,{fileName:"/Users/admin/Documents/te-kete-ako-clean/src/components/PrintableWorksheet.tsx",lineNumber:76,columnNumber:11},void 0)]},void 0,!0,{fileName:"/Users/admin/Documents/te-kete-ako-clean/src/components/PrintableWorksheet.tsx",lineNumber:74,columnNumber:9},void 0),e.jsxDEV("div",{className:"problem-list",children:l.map((s,t)=>e.jsxDEV("div",{className:"problem-item",children:s.problem},t,!1,{fileName:"/Users/admin/Documents/te-kete-ako-clean/src/components/PrintableWorksheet.tsx",lineNumber:80,columnNumber:13},void 0))},void 0,!1,{fileName:"/Users/admin/Documents/te-kete-ako-clean/src/components/PrintableWorksheet.tsx",lineNumber:78,columnNumber:9},void 0)]},void 0,!0,{fileName:"/Users/admin/Documents/te-kete-ako-clean/src/components/PrintableWorksheet.tsx",lineNumber:73,columnNumber:7},void 0),e.jsxDEV("div",{className:"quiz-section",children:[e.jsxDEV("div",{className:"quiz-header",children:[e.jsxDEV("h3",{children:"Addition Practice"},void 0,!1,{fileName:"/Users/admin/Documents/te-kete-ako-clean/src/components/PrintableWorksheet.tsx",lineNumber:86,columnNumber:11},void 0),e.jsxDEV("p",{children:"Name: _______________"},void 0,!1,{fileName:"/Users/admin/Documents/te-kete-ako-clean/src/components/PrintableWorksheet.tsx",lineNumber:87,columnNumber:11},void 0)]},void 0,!0,{fileName:"/Users/admin/Documents/te-kete-ako-clean/src/components/PrintableWorksheet.tsx",lineNumber:85,columnNumber:9},void 0),e.jsxDEV("div",{className:"problem-list",children:o.map((s,t)=>e.jsxDEV("div",{className:"problem-item",children:s.problem},t,!1,{fileName:"/Users/admin/Documents/te-kete-ako-clean/src/components/PrintableWorksheet.tsx",lineNumber:91,columnNumber:13},void 0))},void 0,!1,{fileName:"/Users/admin/Documents/te-kete-ako-clean/src/components/PrintableWorksheet.tsx",lineNumber:89,columnNumber:9},void 0)]},void 0,!0,{fileName:"/Users/admin/Documents/te-kete-ako-clean/src/components/PrintableWorksheet.tsx",lineNumber:84,columnNumber:7},void 0)]},void 0,!0,{fileName:"/Users/admin/Documents/te-kete-ako-clean/src/components/PrintableWorksheet.tsx",lineNumber:18,columnNumber:5},void 0)},b=()=>{const[n,i]=a.useState([]),[l,o]=a.useState(!0),[s,t]=a.useState(null);return a.useEffect(()=>{(async()=>{try{const r=await fetch("/generated_maths_questions.json");if(!r.ok)throw new Error("Failed to fetch maths questions");const m=await r.json();i(m)}catch(r){t(r.message)}finally{o(!1)}})()},[]),l?e.jsxDEV("div",{children:"Loading worksheet..."},void 0,!1,{fileName:"/Users/admin/Documents/te-kete-ako-clean/src/pages/MathsDrillsPage.tsx",lineNumber:34,columnNumber:12},void 0):s?e.jsxDEV("div",{children:["Error: ",s]},void 0,!0,{fileName:"/Users/admin/Documents/te-kete-ako-clean/src/pages/MathsDrillsPage.tsx",lineNumber:38,columnNumber:12},void 0):e.jsxDEV("div",{className:"container mx-auto p-4",children:[e.jsxDEV("h1",{className:"text-2xl font-bold mb-4",children:"Printable Addition Worksheet"},void 0,!1,{fileName:"/Users/admin/Documents/te-kete-ako-clean/src/pages/MathsDrillsPage.tsx",lineNumber:43,columnNumber:7},void 0),e.jsxDEV("p",{className:"mb-4",children:"This worksheet is designed to be printed on A4 paper in landscape orientation. You can then cut it down the middle to create two A5 quizzes. Use your browser's print function (Ctrl/Cmd + P) to print."},void 0,!1,{fileName:"/Users/admin/Documents/te-kete-ako-clean/src/pages/MathsDrillsPage.tsx",lineNumber:44,columnNumber:7},void 0),e.jsxDEV(c,{problems:n},void 0,!1,{fileName:"/Users/admin/Documents/te-kete-ako-clean/src/pages/MathsDrillsPage.tsx",lineNumber:48,columnNumber:7},void 0)]},void 0,!0,{fileName:"/Users/admin/Documents/te-kete-ako-clean/src/pages/MathsDrillsPage.tsx",lineNumber:42,columnNumber:5},void 0)};export{b as MathsDrillsPage,b as default};
