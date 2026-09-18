\# NEORUINS Development Guide



Version 1.0.0



This document describes the development structure, dependencies, local data model, testing practices, and safety expectations for NEORUINS Creator Edition.



\---



\# 1. Project Overview



NEORUINS is a Python command-line application designed to assist gaming creators with:



\- Content generation

\- Draft management

\- Content scheduling

\- X publishing

\- Performance tracking

\- Analytics

\- Data-based content insights



The v1.0.0 application is primarily contained in:



```text

main.py

```



Future versions may separate the application into multiple modules as the project grows.



\---



\# 2. Python Version



NEORUINS v1.0.0 was developed and tested using Python 3.12.



On Windows, the recommended development command is:



```powershell

py -V:3.12 main.py

```



Check the installed version with:



```powershell

py -V:3.12 --version

```



\---



\# 3. Dependencies



Python dependencies are listed in:



```text

requirements.txt

```



Install them with:



```powershell

py -m pip install -r requirements.txt

```



NEORUINS v1.0.0 uses:



```text

tweepy

python-dotenv

```



Tweepy provides the X API interface.



`python-dotenv` loads local environment variables from `.env`.



\---



\# 4. Environment Variables



NEORUINS expects:



```text

X\_API\_KEY

X\_API\_KEY\_SECRET

X\_ACCESS\_TOKEN

X\_ACCESS\_TOKEN\_SECRET

```



These values must be stored in:



```text

.env

```



A safe public template is provided as:



```text

.env.example

```



Never hardcode real credentials into Python source files.



Never commit `.env`.



\---



\# 5. Local Data Files



NEORUINS uses local text files for persistent application data.



Current runtime files include:



```text

approved\_posts.txt

content\_history.txt

drafts.txt

performance\_history.txt

published\_posts.txt

```



These files are excluded from Git because they may contain account-specific or creator-specific information.



The application is designed to handle missing runtime files and create or update relevant files as features are used.



\---



\# 6. Main Application Areas



The current application can be viewed as several functional layers.



\## Content Layer



Responsible for:



\- Gaming-topic input

\- Post-type selection

\- Post generation

\- Rule-based scoring

\- Quality checks

\- Duplicate-content checks

\- Approval

\- Content history



\## Draft and Scheduling Layer



Responsible for:



\- Draft storage

\- Draft editing

\- Scheduling

\- Unscheduling

\- Schedule conflicts

\- Posting-frequency warnings

\- Content calendar

\- Due-post detection



\## X Integration Layer



Responsible for:



\- Loading X credentials

\- Authentication

\- Publishing

\- Recording X Post IDs

\- Retrieving available X metrics



\## Performance Layer



Responsible for:



\- Manual performance entry

\- X API performance retrieval

\- Performance-history storage

\- Performance scoring



\## Analytics Layer



Responsible for:



\- Overall performance analytics

\- Post-type analytics

\- Posting-time analytics

\- Posting-hour analytics

\- Posting-day analytics

\- Schedule insights

\- Content strategy insights

\- Combined content-type and schedule insights



\---



\# 7. Content Types



NEORUINS v1.0.0 supports:



```text

Gaming Question

Hot Take

News Reaction

Streaming Post

Meme Style

```



When modifying content generation, preserve compatibility with existing analytics and stored records that reference these names.



Changing a Post type name may affect historical-data matching.



\---



\# 8. Rule-Based Content Scoring



Generated Posts receive a local rule-based engagement score.



The current system considers characteristics such as:



\- Whether the Post contains a question

\- Whether it remains within the expected Post length

\- Whether it contains a hashtag

\- Whether it uses reader-focused language

\- Whether it contains enough words



This score evaluates the structure of generated content.



It is not a machine-learning prediction and does not guarantee X engagement.



When changing the scoring system, test existing generation and review workflows.



\---



\# 9. Performance Scoring



NEORUINS also contains a separate performance score for tracked Posts.



Do not confuse:



```text

Generated Post Score

```



with:



```text

Performance Score

```



The performance score uses observed engagement relative to views and applies additional weighting to certain engagement actions.



The v1.0.0 score is capped at 100.



Developers should be aware that small view counts can produce unusually high scores.



Improving this scoring model is a potential future development area.



\---



\# 10. X API Integration



X integration uses Tweepy and credentials loaded from environment variables.



Publishing and metric retrieval should never require credentials to be written directly into source code.



API behavior, permissions, limits, and available metrics can change independently of NEORUINS.



When modifying X integration:



1\. Review current official X Developer documentation.

2\. Test authentication separately.

3\. Avoid unnecessary live publishing.

4\. Verify the correct account before testing publication.

5\. Never commit credentials.

6\. Preserve safe failure behavior when API requests fail.



See:



```text

docs/X\_API\_SETUP.md

```



\---



\# 11. Human-Controlled Publishing



NEORUINS v1.0.0 is designed around human confirmation before supported publishing actions.



The expected scheduled publishing workflow is:



```text

Draft

&#x20;  ↓

Schedule

&#x20;  ↓

Due

&#x20;  ↓

Review

&#x20;  ↓

Confirm

&#x20;  ↓

Publish

```



Developers should not silently remove confirmation safeguards when modifying the publishing system.



Changes involving automated publishing should be treated as significant product-design changes and tested separately.



\---



\# 12. Published Post Records



Successful publishing information is stored in:



```text

published\_posts.txt

```



These records allow NEORUINS to associate local content with an X Post ID.



That association is used by performance tracking to determine whether live X metrics can be requested.



Changes to the published-record format should preserve backward compatibility where practical.



\---



\# 13. Performance Records



Performance information is stored in:



```text

performance\_history.txt

```



Records may originate from:



```text

Manual Entry

```



or:



```text

X API

```



The data source is important.



The real-X recommendation system uses X API records when generating its real-data guidance so that legacy or manually entered records do not silently distort those recommendations.



Developers modifying performance parsing should preserve this distinction.



\---



\# 14. Analytics and Sample Size



Several analytics features depend on publication timestamps and accumulated performance records.



Some insight features intentionally require minimum sample sizes before generating stronger observations.



Developers should preserve this principle:



```text

Small samples should not be presented as reliable long-term strategy.

```



Analytics output should distinguish observations from guarantees.



\---



\# 15. Date and Time Handling



Scheduled drafts use:



```text

YYYY-MM-DD HH:MM

```



Publication timestamps used by analytics also rely on consistent date/time formatting.



When live X metrics provide a creation timestamp, NEORUINS converts the timestamp for use with its existing local posting-time analytics.



Changes to time handling should be tested carefully because they can affect:



\- Scheduling

\- Due-post detection

\- Hour analytics

\- Day analytics

\- Schedule insights



\---



\# 16. Backward Compatibility



NEORUINS has evolved through multiple development versions.



Some parsers include compatibility behavior for older local record formats.



Do not remove legacy parsing solely because the current writer uses a newer structure.



Before changing a storage format:



1\. Identify existing readers.

2\. Identify existing writers.

3\. Test older records where applicable.

4\. Avoid destroying user data.

5\. Create a migration strategy if compatibility must be broken.



\---



\# 17. Development Backups



Before making significant changes to `main.py`, create a backup.



Example:



```powershell

Copy-Item main.py backups\\main\_before\_change.py

```



Backup files should remain local.



The repository `.gitignore` excludes:



```text

backups/

main\_\*\_backup.py

```



Do not publish backups containing development data or experimental credentials.



\---



\# 18. Syntax Testing



After changing Python code, run:



```powershell

py -V:3.12 -m py\_compile main.py

```



A successful command with no Python error indicates that the file compiled successfully.



Compilation does not prove that every workflow works correctly.



Runtime testing is still required.



\---



\# 19. Startup Testing



After compilation, start NEORUINS:



```powershell

py -V:3.12 main.py

```



Verify:



\- Startup completes

\- Schedule check completes

\- All expected menu options appear

\- No unexpected traceback occurs

\- Exit works normally



\---



\# 20. Workflow Testing



Test the workflow affected by your change.



Examples include:



```text

Generate → Review → Cancel

```



```text

Generate → Draft → Schedule

```



```text

Draft → Review → Approve

```



```text

Approved Post → Publishing Review

```



```text

Published Post → Performance Tracking

```



Prefer non-destructive tests whenever possible.



\---



\# 21. Live X Testing



Live publishing should be used only when necessary.



Before performing a live test:



\- Confirm the connected account

\- Review the exact Post

\- Confirm that a live Post is actually required

\- Avoid repeated unnecessary API calls

\- Be aware of applicable X API usage or costs



Never publish a test Post accidentally just to verify that a menu loads.



\---



\# 22. Test Utilities



Development utilities may be stored under:



```text

tests/

```



Before publishing a test file to GitHub, inspect it for:



\- Hardcoded X Post IDs

\- Account-specific identifiers

\- API credentials

\- Tokens

\- Personal data

\- Temporary debugging information



Public test utilities should use environment variables or clearly marked example values where configuration is necessary.



\---



\# 23. Secret Scanning



Before creating a public release, inspect the repository for secrets.



At minimum, verify that:



```text

.env

```



is ignored and is not staged for Git.



Also inspect source code, tests, examples, and documentation for accidentally copied credentials.



If a real credential ever enters public Git history, deleting it from the newest file is not sufficient.



Treat exposed credentials as compromised and revoke or regenerate them.



\---



\# 24. Files That Must Remain Private



The following development files or folders should not be included in the public v1.0.0 repository:



```text

.env

backups/

local\_data\_backup/

```



Local runtime data should also remain excluded:



```text

approved\_posts.txt

content\_history.txt

drafts.txt

performance\_history.txt

published\_posts.txt

```



\---



\# 25. Repository Documentation



Public documentation includes:



```text

README.md

LICENSE.md

CHANGELOG.md

ROADMAP.md

SECURITY.md

CONTRIBUTING.md

docs/INSTALLATION.md

docs/CONFIGURATION.md

docs/X\_API\_SETUP.md

docs/USER\_GUIDE.md

docs/DEVELOPMENT.md

```



Keep documentation synchronized with actual application behavior.



Do not document planned features as if they already exist.



\---



\# 26. Versioning



The first public Creator Edition release is:



```text

v1.0.0

```



Future releases should document significant changes in:



```text

CHANGELOG.md

```



Release plans may also be reflected in:



```text

ROADMAP.md

```



\---



\# 27. Contribution Expectations



Contributors should:



\- Preserve existing functionality

\- Protect user credentials

\- Avoid unnecessary breaking changes

\- Test modified workflows

\- Document meaningful changes

\- Respect the project's licensing terms



See:



```text

CONTRIBUTING.md

```



\---



\# 28. Licensing



NEORUINS Creator Edition is distributed under the terms contained in:



```text

LICENSE.md

```



Do not assume that public source availability means the project is open source.



Review the license before redistributing, modifying, or using NEORUINS for commercial purposes.



\---



\# 29. Development Priorities



Future development should continue prioritizing:



\- Creator control

\- Credential security

\- Reliable publishing workflows

\- Backward compatibility

\- Useful analytics

\- Appropriate sample-size handling

\- Clear separation between observed data and predictions

\- Maintainable code structure



\---



\# 30. Release Checklist



Before publishing a new release:



```text

\[ ] Create a backup

\[ ] Run Python compilation test

\[ ] Test application startup

\[ ] Verify expected menu options

\[ ] Test changed workflows

\[ ] Verify .env is ignored

\[ ] Verify local data is ignored

\[ ] Inspect tests for private information

\[ ] Scan repository for credentials

\[ ] Review documentation

\[ ] Update CHANGELOG.md

\[ ] Confirm version number

\[ ] Review Git staging area

\[ ] Create release only after checks pass

```



\---



\# NEORUINS Creator Edition



Version 1.0.0



Copyright © 2026 Angelo Padula



All rights reserved.
