![Nancy Verma. AI and ML, software engineering, and geospatial work. Manipal University Jaipur, Grids App LLC, Jaipur, India.](./assets/header.png)

[![Portfolio](https://img.shields.io/badge/portfolio-live-6b3fa0?style=flat-square)](https://nancy-portfolio-new.vercel.app)
[![License: MIT](https://img.shields.io/badge/license-MIT-c9a227?style=flat-square)](./LICENSE)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Nancy%20Verma-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/nancy-verma)
[![LeetCode](https://img.shields.io/badge/LeetCode-Nancy2005-FFA116?style=flat-square)](https://leetcode.com/u/Nancy2005)
[![Python](https://img.shields.io/badge/Python-3-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5-3178C6?style=flat-square&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![Next.js](https://img.shields.io/badge/Next.js-16-000000?style=flat-square&logo=nextdotjs&logoColor=white)](https://nextjs.org/)

# Nancy Verma

Aspiring software engineer and AI & ML student, charting a path through code, remote sensing, and human-centered tools. Google WE Scholar. I build things that turn a question into something a person can use.

Portfolio: <https://nancy-portfolio-new.vercel.app> · LinkedIn: <https://linkedin.com/in/nancy-verma> · LeetCode: <https://leetcode.com/u/Nancy2005> · Email: nancy2005nov@gmail.com

## Contents

- [Skills](#skills)
- [Experience](#experience)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Research](#research)
- [GitHub](#github)
- [References](#references)
- [License](#license)

## Skills

![Python, C++, JavaScript, TypeScript, HTML, CSS, React, Next.js, Tailwind, Flask, TensorFlow, PyTorch, Git, and Docker](https://skillicons.dev/icons?i=py,cpp,js,ts,html,css,react,nextjs,tailwind,flask,tensorflow,pytorch,git,docker)

| Area | Tools |
| --- | --- |
| Languages | Python, C++, JavaScript, TypeScript, HTML, CSS |
| Machine learning | TensorFlow, Keras, scikit-learn, PyTorch |
| Web | React, Next.js, Tailwind, Flask |
| Geospatial | Google Earth Engine, GIS |
| Tools | Git, Docker, Google Colab, LaTeX, VS Code |

## Experience

| Role | Organization | When |
| --- | --- | --- |
| Software engineering intern | Grids App LLC | Present |
| B.Tech, Artificial Intelligence & Machine Learning. CGPA 9.79 / 10. Dean's List and Dr. TMA Pai Merit Scholarship | Manipal University Jaipur | 2023–2027 |
| Google WE Scholar, selected from over 30,000 applicants, plus Google Immersion Week | Google and TalentSprint | 2024 |
| SheFi Scholar, smart contracts and decentralized applications | SheFi | 2024 |
| Remote sensing and GIS intern | India Space Academy | May–July |

## Features

| Project | What it does | Try it |
| --- | --- | --- |
| [FinSight](https://github.com/Nancy20052020/finsight_off) | Schedule-aware cash-flow forecast. Bills and invoices sit on their real dates, and on the sample books the forecast flags a shortfall the trailing-average baseline misses. | [Live](https://finsight-off.vercel.app) |
| [AutEye](https://github.com/Nancy20052020/Autism_eye) | Eye-tracking and machine learning for early autism screening, aimed at clearer signals for caregivers and clinicians. Sibling work to a patent filed in India and Germany. | [Source](https://github.com/Nancy20052020/Autism_eye) |
| [Grids Gold](https://github.com/Nancy20052020/GridsGold) | Jewellery ERP dashboard for inventory, catalogue, and accounts. | [Live](https://grids-gold.vercel.app) |
| [TREADURE](https://github.com/Nancy20052020/Nancy_portfolio_new) | Quest-map portfolio in Next.js, Tailwind, GSAP, and Framer Motion. | [Live](https://nancy-portfolio-new.vercel.app) |
| [Multi PDF Bot](https://github.com/Nancy20052020/Mutli_PDF_BOT) | Ask questions across uploaded PDFs. Answers come from GPT-3.5 and are spoken with ElevenLabs. | [Source](https://github.com/Nancy20052020/Mutli_PDF_BOT) |
| [Braille](https://github.com/Nancy20052020/Braille) | Browser tools so written text can be read by touch or heard aloud. | [Source](https://github.com/Nancy20052020/Braille) |

Geospatial work from the India Space Academy internship:

| Study | What it maps |
| --- | --- |
| [Drought Sentinel](https://drive.google.com/file/d/1RZha6dBhiwGYqZHKaGM_WiZF5jK6NnmV/view) | Drought analysis from satellite imagery in Google Earth Engine |
| [Urban Pulse](https://drive.google.com/file/d/1TFvuLC2Rm8a2FTUSVplmug-8RdcGejW3/view) | Urban maps of city signals |

## Installation

Node.js 20 or newer is required for the Next.js projects. The portfolio installs from GitHub:

```bash
git clone https://github.com/Nancy20052020/Nancy_portfolio_new.git
cd Nancy_portfolio_new
npm install
npm run dev
```

FinSight uses the same install, and it does not need API keys. The sample books in `data/` are read when the site builds, and the forecast runs in the browser.

```bash
git clone https://github.com/Nancy20052020/finsight_off.git
cd finsight_off
npm install
npm run dev
```

Open <http://localhost:3000> for either app.

## Usage

On the portfolio, the map pins open skills, projects, publications, experience, achievements, and contact. Light and dark themes share the same pages.

FinSight's check compares the TypeScript engine with the Python engine:

```bash
npm run parity
PYTHONPATH=src python -m unittest tests.test_cash
```

The holdout helper below is from [`finsight_off/lib/evaluate.ts`](https://github.com/Nancy20052020/finsight_off/blob/main/lib/evaluate.ts). It freezes the books at an origin date so the forecast is scored only on what was already known:

```ts
function booksAsOf(
  transactions: Transaction[],
  invoices: Invoice[],
  origin: string,
): { transactions: Transaction[]; invoices: Invoice[] } {
  return {
    transactions: transactions.filter((row) => row.date <= origin),
    invoices: invoices
      .filter((invoice) => invoice.issue_date <= origin)
      .map((invoice) => ({
        ...invoice,
        paid_date: invoice.paid_date && invoice.paid_date > origin ? null : invoice.paid_date,
      })),
  };
}
```

Earlier experiments, not part of the install above: [Snake](https://github.com/Nancy20052020/snake_game) and [Pong](https://github.com/Nancy20052020/Ping_Pong) in Python with `turtle`, and the [first portfolio](https://nancy20052020.github.io/Portfolio).

## Research

| Kind | Title | Where |
| --- | --- | --- |
| Publication | Enhancing Fish Species Recognition: Deep Learning Models Evaluation. Compared ResNet, VGG16, InceptionV3, and a CNN for underwater fish classification, with 95%+ accuracy and notes on training cost. | IEEE ICDSNS 2024 |
| Patent | Autism Detection through Eye Tracking. An eye-tracking pipeline for early autism-related gaze signals. | Filed in India and Germany |

Hackathons: IIC Top 17%, Prastuti finalist, IES MCRC 2nd place.

## GitHub

![All-time GitHub stats for Nancy Verma](./assets/github-stats-light.png)

![Languages most used by Nancy Verma](https://github-readme-stats.vercel.app/api/top-langs/?username=Nancy20052020&layout=compact&hide_border=true&langs_count=6&title_color=6b3fa0&text_color=3d2914&bg_color=f7f1e6)

## References

| | |
| --- | --- |
| Portfolio | <https://nancy-portfolio-new.vercel.app> |
| FinSight | <https://finsight-off.vercel.app> |
| Grids Gold | <https://grids-gold.vercel.app> |
| Drought Sentinel notes | <https://drive.google.com/file/d/1RZha6dBhiwGYqZHKaGM_WiZF5jK6NnmV/view> |
| Urban Pulse notes | <https://drive.google.com/file/d/1TFvuLC2Rm8a2FTUSVplmug-8RdcGejW3/view> |
| Next.js docs | <https://nextjs.org/docs> |
| Google Earth Engine | <https://developers.google.com/earth-engine> |
| IEEE ICDSNS | <https://ieeexplore.ieee.org/> |

## License

This profile repository is released under the [MIT License](./LICENSE). Copyright 2026 Nancy Verma. Project repositories keep their own licenses.
