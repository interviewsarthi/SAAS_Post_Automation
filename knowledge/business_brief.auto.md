# InterviewSarthi: auto brief
Generated 01 November 2026 from 40 pages of https://interviewsarthi.com.

## One line
InterviewSarthi offers three developer-built AI apps to help job seekers find jobs, practise mock interviews, and receive real-time call assistance.

## What it does, in detail
InterviewSarthi provides a suite of three separate job-search tools built by an independent software developer in India:

* ApplySarthi: Aggregates job postings from Naukri, LinkedIn, Indeed, Foundit, Shine, Internshala, Wellfound, and over 754 company career boards. It matches open roles to the candidate's CV, tailors CVs and cover letters, and autofills application forms using a Chrome browser extension. It includes a browser-based ATS resume checker and an optional Autopilot mode for automatic form submission.
* PrepSarthi: Conducts interactive, spoken AI mock interviews using the candidate's CV and target job description. It asks custom questions, targets weak answers with follow-ups, and provides detailed performance feedback.
* LiveSarthi: Runs as a Windows desktop application during live interview calls. It listens to spoken interview questions and displays context-aware answer suggestions on screen in English, Hindi, or Hinglish, while remaining hidden from supported screen-sharing tools.

## How it works (technology, privacy, requirements)
* AI Technology: Powered by Google Gemini. Users supply their own free Google Gemini API key for paid passes and advanced features (Prep free demo and basic job browsing do not require a key).
* System Requirements: ApplySarthi requires desktop Google Chrome for autofill; PrepSarthi runs in any standard web browser with microphone access on mobile or desktop; LiveSarthi requires Windows 10 (version 2004 or newer) or Windows 11. LiveSarthi does not support macOS.
* Open Source Transparency: LiveSarthi Windows releases are published openly on GitHub with public version histories.
* Privacy and Data Handling: 
  * The ATS Resume Checker processes files (.pdf and .docx up to 5 MB) locally inside the user browser tab using PDF.js and Mammoth. Files are never uploaded, stored, or transmitted to servers.
  * ApplySarthi performs form filling inside the user own browser using active logged-in sessions. Account passwords for job portals like Naukri or LinkedIn are never requested or stored.
  * LiveSarthi uses standard Windows capture protection APIs to hide its answer panel from supported screen sharing. No automated bot joins the call.
* Resume Grounding: CV tailoring and live answer tools strictly enforce source verification. Rewritten bullet points that invent numbers, metrics, or facts absent from the original CV are automatically discarded.

## Pricing (exact numbers and terms as published)
Pages contain minor variations regarding promotional dates and response latencies; the newest dates and numbers are listed below.

* ApplySarthi:
  * Always free. No paid tier, no subscription, no credit card required. First tailored CV is free; subsequent CV tailoring uses the candidate's own free Gemini key.
* PrepSarthi:
  * Free trial: 7-minute demo interview (no sign-up, no Gemini key required).
  * 30-Day Unlimited Pass: ₹99 one-time payment (uses candidate Gemini key). Included free with Live Sarthi 1-Month Pass until 30 November 2026.
* LiveSarthi (India Pricing):
  * Free trial: 30 minutes free total allowance per Windows device.
  * Diwali Promotional 2-Day Pass: ₹99 until 10 November 2026 (increases to ₹149 from 11 November 2026). Keys can be bought in advance and activated within 30 days of purchase; the 48-hour access starts upon key entry in the app.
  * Regular 2-Day Pass: ₹99 for 2 days of unlimited interviews on 1 device.
  * 1-Month Pass: ₹299 for 30 days of unlimited interviews on 2 devices (includes free 30-day Prep Sarthi pass worth ₹99 until 30 November 2026).
* LiveSarthi (International Pricing):
  * 30-Day Pass: $29.99 for 30 days of unlimited use on 2 devices.
* Payment Terms:
  * Passes do not auto-renew and have no recurring commitments.
  * Google Gemini API quotas and any third-party API usage fees are separate from InterviewSarthi passes.

## Who it is for
* Job seekers in India and internationally across technical, data, product, QA, and finance roles.
* Freshers seeking to structure project explanations, experienced professionals organising career achievements, and candidates re-entering the workforce after a gap.
* Candidates applying heavily on Indian job portals (Naukri, Foundit, Shine, Internshala) alongside ATS career portals (Greenhouse, Lever, Ashby, Workday).
* Applicants looking for spoken mock practice or real-time call guidance in English, Hindi, or Hinglish on Windows PCs.

## Problems it solves
* Time lost manually searching across multiple fragmented job boards.
* Repetitive text entry on long job application forms.
* High application rejection rates caused by generic CVs failing parser keyword searches.
* Scrambled or misread CV data caused by incompatible multi-column ATS layouts.
* Lack of access to a practice partner for spoken interview rehearsals.
* Live interview pressure, memory blanks, and difficulty structuring answers during calls.
* Inability of standard server-side auto-apply tools to access protected Indian job boards like Naukri and Foundit.

## Differentiators and proof points (only what the site states)
* Single Developer Accountability: Built and supported by one independent developer in India who handles code and customer support directly.
* Verified Indian Portal Access: Uses real browser automation to fill forms on Naukri, Foundit, Shine, and Internshala, which block server-side headless browsers used by international competitors.
* Hallucination Prevention: Code rules actively drop AI-generated lines that introduce fabricated numbers, dates, or credentials not found in the source document.
* Real-time Response Speed: Answer suggestions begin appearing in about 1 second (noted as 1.5 seconds under specific test conditions on the About page).
* Screen Share Concealment: Live answer window remains invisible to meeting software using standard Windows capture protection.
* Local Browser Processing: ATS checker runs completely client-side without file uploads.
* Transparent Open Releases: Windows installers are published on GitHub with verifiable release logs.

## Voice, tone and words the site uses
* Tone: Practical, transparent, direct, pragmatic, source-focused, developer-led.
* Core Brand Word: "Sarthi" (सारथी), defined as charioteer or guide.
* Key Phrases: "Say this", "Resume grounding", "Your career. Your call.", "Less typing. More progress.", "No bot joining the call", "Hidden from supported screen sharing", "Your CV stays on your device", "No auto-renewal".

## Words and claims the site avoids or warns about
* Avoids placing success metrics: Explicitly states that no benchmark rankings, detection rates, or guaranteed interview/offer percentages are claimed.
* Warns against bulk tools: Criticises tools promising 1,500 automated submissions a day for spamming recruiters and risking account bans.
* Rejects auto-rejection myths: Clarifies that ATS software parses and stores resumes for human search rather than automatically issuing rejection scores.
* Strictly prohibits fabrication: Warns candidates never to add unearned skills, fake metrics, or unverified work dates to their CVs.
* Warns on permissions: Explicitly instructs candidates to use live call assistance only where employer and interviewer rules permit it.

## Links worth pointing to (URL: what it is)
* https://interviewsarthi.com : Primary portal for Live Sarthi and product overview.
* https://interviewsarthi.com/about.html : Developer story, business model details, privacy practices, and support contact info.
* https://interviewsarthi.com/apply/ : ApplySarthi job engine and Chrome extension download.
* https://interviewsarthi.com/apply/ats-resume-checker/ : Free client-side ATS resume parser tool.
* https://interviewsarthi.com/best-ai-interview-assistant-india.html : Comparison guide reviewing public prices of Indian interview assistants.
* https://interviewsarthi.com/apply/guides/ : Educational index for ATS formatting, Naukri automation, and application strategy.
* https://interviewsarthi.com/apply/is-auto-apply-safe.html : Technical breakdown of application safety, privacy, and account limits.
* https://interviewsarthi.com/apply/job-application-statistics-india.html : Analysis of 60,975 open Indian job listings.

## Frequently asked questions (as answered on the site)
* What does InterviewSarthi do? It provides three distinct tools: ApplySarthi to aggregate jobs and autofill forms, PrepSarthi to run spoken AI mock interviews, and LiveSarthi to display call suggestions on Windows.
* Does Live Sarthi appear in screen sharing? It hides its answer panel from supported Windows 10 (2004+) and Windows 11 capture APIs. Candidates must test their meeting setup prior to live calls.
* How fast does Live Sarthi present answers? Answer suggestions begin appearing on screen in approximately 1 to 1.5 seconds depending on model, network connection, and question complexity.
* Is ApplySarthi free? Yes, ApplySarthi is always free with no paid plan or subscription required.
* Are uploaded resumes saved on the ATS checker? No. Files are processed entirely inside the browser tab using PDF.js and Mammoth and are deleted upon closing the tab.
* Can tools auto-apply on Naukri from a server? No. Naukri blocks plain HTTP requests and headless server browsers. Automation requires driving a visible Chromium browser window locally.
* Do passes renew automatically? No. PrepSarthi and LiveSarthi passes are one-time payments for fixed validity periods and never auto-renew.

## Content angles suggested by the site's own pages
* "The 1,500-a-day Trap": Explaining why bulk submission tools cause duplicate recruiter flags and account limits, whereas targeted browser autofill preserves candidate credibility.
* "Why International Auto-Apply Tools Fail in India": Technical breakdown showing why server-side platforms cannot access Naukri or Foundit.
* "5 Reasons 200 Applications Produced Zero Calls": Actionable audit covering stale listings (only 5.7% list closing dates), unparsed two-column layouts, and generic resumes.
* "How to Format an ATS-Friendly Resume in India": Practical formatting advice including removing photos, declarations, personal details, and two-column tables.
* "Mock Interviews vs Live Call Assistance": Clarifying when to use voice rehearsal tools versus permitted real-time call guidance in Hinglish.

## Open questions the owner should confirm
* Confirm the price transition for the Live Sarthi 2-Day Pass (verifying whether the rate moved from ₹99 to ₹149 following 10 November 2026).
* Clarify exact international pricing tiers across non-INR currencies outside the cited $29.99 30-day plan.
* Confirm whether support for non-Windows desktop platforms (macOS, Linux) is planned for LiveSarthi.
