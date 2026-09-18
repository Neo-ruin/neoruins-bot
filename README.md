# NEORUINS Bot v1.0.0

## AI-Assisted Gaming Social Media Manager

NEORUINS is a Python-based gaming content management system designed to help creators generate, organize, schedule, publish, and analyze content for X.

Built for gaming creators, streamers, and online communities, NEORUINS combines content-generation tools with a human-controlled publishing workflow and performance analytics.

---

# Features

## Content Generation

- Gaming-focused post creation
- Five supported content formats
- Brand voice system
- Rule-based content scoring
- Duplicate-content checks
- Review and approval workflow
- Draft storage

Supported post types:

- Gaming Question
- Hot Take
- News Reaction
- Streaming Post
- Meme Style

---

## Drafts and Scheduling

- Draft management
- Draft editing
- Scheduled posts
- Unscheduling
- Content calendar
- Schedule conflict detection
- Posting-frequency warnings
- Due-post review
- Startup schedule check

Scheduling does not silently publish a Post.

Due Posts are surfaced for review before publication.

---

## X Integration

NEORUINS v1.0.0 includes integration with the X API through Tweepy.

Features include:

- OAuth 1.0a user authentication
- Account verification
- Human-confirmed publishing
- Published Post ID tracking
- Live performance metric retrieval
- X publication timestamp retrieval

Your own X Developer credentials are required for X API features.

---

## Performance Tracking

NEORUINS can track available performance information such as:

- Views
- Likes
- Reposts
- Replies
- Bookmarks
- Engagement activity

Performance information can come from supported X API retrieval or manual entry.

---

## Analytics and Insights

NEORUINS includes:

- Performance Analytics
- Post Type Analytics
- Performance Insights
- Posting Time Analytics
- Posting Hour Analytics
- Posting Hour Insights
- Posting Day Analytics
- Posting Day Insights
- Posting Schedule Insights
- Content Strategy Insights
- Content Type + Schedule Insights

The system uses accumulated performance records to provide observations about content and posting patterns.

Analytics should not be treated as guaranteed predictions of future engagement, especially when only a small amount of data is available.

---

# Human-Controlled Publishing

NEORUINS is designed to keep the creator in control of publishing.

The intended workflow is:

```text
Generate
   ↓
Review
   ↓
Approve
   ↓
Schedule or Select
   ↓
Review for Publishing
   ↓
Confirm
   ↓
Publish to X
```

NEORUINS v1.0.0 does not silently publish scheduled Posts through its normal scheduled-post workflow.

---

# Requirements

NEORUINS v1.0.0 was developed and tested with:

- Windows
- Python 3.12
- Tweepy
- python-dotenv

X API features additionally require:

- An X Developer account
- An X Developer application
- Appropriate X API access and permissions
- Your own API credentials

X controls, API capabilities, limits, and pricing may change independently of NEORUINS.

Refer to the current official X Developer documentation before configuring or purchasing API access.

---

# Installation

Clone the repository:

```powershell
git clone YOUR_REPOSITORY_URL
cd neoruins-bot
```

The final repository URL will replace the placeholder after the public GitHub repository is created.

Install dependencies:

```powershell
py -m pip install -r requirements.txt
```

Create your private environment file:

```powershell
Copy-Item .env.example .env
```

Then add your own X API credentials to `.env`.

Never commit or publicly share your `.env` file.

For complete setup instructions, see:

```text
docs/INSTALLATION.md
docs/CONFIGURATION.md
docs/X_API_SETUP.md
```

---

# Running NEORUINS

On Windows with Python 3.12 installed:

```powershell
py -V:3.12 main.py
```

If Python 3.12 is already your default Python installation, you may also use:

```powershell
py main.py
```

The interactive menu provides access to content generation, draft management, scheduling, publishing, performance tracking, analytics, and insights.

---

# Main Menu

NEORUINS Creator Edition v1.0.0 contains 22 main menu options:

```text
1. Generate New Post
2. View Approved Posts
3. View Content History
4. View Drafts
5. Review Drafts
6. Content Calendar
7. Manage Drafts
8. Track Post Performance
9. View Performance History
10. Performance Analytics
11. Post Type Analytics
12. Performance Insights
13. Posting Time Analytics
14. Posting Hour Analytics
15. Posting Hour Insights
16. Posting Day Analytics
17. Posting Day Insights
18. Posting Schedule Insights
19. Content Strategy Insights
20. Content Type + Schedule Insights
21. X Publishing Layer
22. Exit
```

See `docs/USER_GUIDE.md` for detailed instructions.

---

# Project Structure

```text
neoruins-bot/
│
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
│
├── README.md
├── LICENSE.md
├── CHANGELOG.md
├── ROADMAP.md
├── SECURITY.md
├── CONTRIBUTING.md
│
├── docs/
│   ├── INSTALLATION.md
│   ├── CONFIGURATION.md
│   ├── X_API_SETUP.md
│   ├── USER_GUIDE.md
│   └── DEVELOPMENT.md
│
└── tests/
    ├── test_x_connection.py
    └── x_metrics_test.py
```

Private local files such as `.env`, development backups, and runtime data are intentionally excluded from the public repository.

---

# Local Runtime Data

During normal use, NEORUINS may create or update:

```text
approved_posts.txt
content_history.txt
drafts.txt
performance_history.txt
published_posts.txt
```

These files are stored locally in the project directory in v1.0.0.

They are excluded from Git by `.gitignore` because they may contain creator-specific or account-specific information.

---

# X Publishing Layer

The X Publishing Layer provides:

```text
1. Publish an Approved Post
2. Review Due Scheduled Posts
0. Return
```

Publishing actions require user review and confirmation.

For X integration instructions, see:

```text
docs/X_API_SETUP.md
```

---

# Testing

Development utilities are located in:

```text
tests/
```

The metrics utility retrieves information for an existing X Post and does not publish or modify the Post.

The live publishing utility can create a real public X Post and requires explicit confirmation before publishing.

Use live X tests carefully.

For development and testing guidance, see:

```text
docs/DEVELOPMENT.md
```

---

# Security

Never publish:

- API keys
- API secrets
- Access tokens
- Access-token secrets
- `.env`
- Private runtime data

NEORUINS uses environment variables to keep credentials separate from source code.

Read:

```text
SECURITY.md
```

before publishing, distributing, or modifying the X integration.

---

# Documentation

Additional documentation is available in:

```text
docs/INSTALLATION.md
docs/CONFIGURATION.md
docs/X_API_SETUP.md
docs/USER_GUIDE.md
docs/DEVELOPMENT.md
```

Project-level documents include:

```text
CHANGELOG.md
ROADMAP.md
SECURITY.md
CONTRIBUTING.md
LICENSE.md
```

---

# Version 1.0.0

NEORUINS Creator Edition v1.0.0 is the first public Creator Edition release.

It includes:

- Gaming content generation
- Draft management
- Scheduling
- Content calendar
- Human-controlled X publishing
- Published Post tracking
- Live X performance retrieval
- Performance history
- Analytics
- Content and schedule insights

See `CHANGELOG.md` for release details.

---

# Roadmap

Future development areas include:

- Advanced content optimization
- Creator assistance tools
- Expanded analytics
- Creator dashboards
- Multi-platform support
- Improved project modularity

Planned features are documented separately from currently available functionality.

See:

```text
ROADMAP.md
```

---

# License

NEORUINS Creator Edition is source-available software distributed under the terms in:

```text
LICENSE.md
```

Public availability of the source code does not mean the project is released under an open-source license.

Review the license before redistributing, modifying, or using the software commercially.

---

# NEORUINS Creator Edition

Version 1.0.0

Copyright © 2026 Angelo Padula

All rights reserved.