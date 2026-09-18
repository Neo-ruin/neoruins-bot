\# NEORUINS Creator Edition User Guide



Version 1.0.0



NEORUINS is a command-line social media management application designed for gaming creators, streamers, and gaming communities.



It provides tools for generating content, managing drafts, scheduling posts, publishing to X, tracking performance, and learning from collected performance data.



\---



\# 1. Starting NEORUINS



Open PowerShell in the NEORUINS project directory.



Run:



```powershell

py -V:3.12 main.py

```



NEORUINS will start and display the main menu.



\---



\# 2. Main Menu



NEORUINS Creator Edition v1.0.0 contains 22 main menu options:



```text

1\. Generate New Post

2\. View Approved Posts

3\. View Content History

4\. View Drafts

5\. Review Drafts

6\. Content Calendar

7\. Manage Drafts

8\. Track Post Performance

9\. View Performance History

10\. Performance Analytics

11\. Post Type Analytics

12\. Performance Insights

13\. Posting Time Analytics

14\. Posting Hour Analytics

15\. Posting Hour Insights

16\. Posting Day Analytics

17\. Posting Day Insights

18\. Posting Schedule Insights

19\. Content Strategy Insights

20\. Content Type + Schedule Insights

21\. X Publishing Layer

22\. Exit

```



Enter the number corresponding to the feature you want to use.



\---



\# 3. Generate New Post



Choose:



```text

1\. Generate New Post

```



NEORUINS displays its configured personality and brand voice and then asks for a gaming topic.



Example:



```text

Enter a gaming topic: Fortnite

```



You then choose one of five content types:



```text

1\. Gaming Question

2\. Hot Take

3\. News Reaction

4\. Streaming Post

5\. Meme Style

```



NEORUINS generates three variations for the selected topic and content type.



Each variation receives a rule-based engagement score.



The scoring system evaluates characteristics such as:



\- Post length

\- Questions

\- Hashtags

\- Reader-focused words

\- Amount of text



NEORUINS also displays its highest-scoring generated variation as a recommendation.



This score is a local rule-based writing score. It is not a prediction or guarantee of real X performance.



You may select one of the three generated posts for review or cancel the generation.



\---



\# 4. Reviewing a Generated Post



After selecting a generated post, NEORUINS displays:



\- The Post

\- Engagement score

\- Quality checks



Available actions are:



```text

1\. Approve

2\. Edit

3\. Save as Draft

4\. Cancel

```



\## Approve



Saves the Post to:



```text

approved\_posts.txt

```



and records it in:



```text

content\_history.txt

```



NEORUINS also checks whether the content appears similar to content already stored locally.



\## Edit



Allows you to rewrite the Post manually.



NEORUINS recalculates the rule-based score after the edit.



\## Save as Draft



Stores the Post in:



```text

drafts.txt

```



You may optionally assign a future scheduled date and time.



\## Cancel



Leaves the review workflow without approving the Post.



\---



\# 5. View Approved Posts



Choose:



```text

2\. View Approved Posts

```



This displays Posts stored in:



```text

approved\_posts.txt

```



Approved Posts are available for later workflows, including publishing and performance tracking.



\---



\# 6. View Content History



Choose:



```text

3\. View Content History

```



This displays the locally stored content history from:



```text

content\_history.txt

```



The history helps maintain a record of previously approved content.



\---



\# 7. View Drafts



Choose:



```text

4\. View Drafts

```



NEORUINS displays currently stored drafts.



Information may include:



\- Topic

\- Post type

\- Score

\- Scheduled date/time

\- Post text



\---



\# 8. Review Drafts



Choose:



```text

5\. Review Drafts

```



Select a draft to review.



Available actions include:



```text

1\. Approve

2\. Edit

3\. Delete

4\. Return

```



Approving a draft moves its content into the approved-post workflow and removes that draft from the draft list.



Editing updates the draft and recalculates its rule-based score.



Deleting permanently removes the selected draft from the active draft file.



\---



\# 9. Content Calendar



Choose:



```text

6\. Content Calendar

```



The Content Calendar displays drafts that have scheduled publication times.



Scheduled Posts are ordered chronologically and grouped by date.



The calendar displays information including:



\- Time

\- Topic

\- Post type

\- Score

\- Post text



Only drafts containing a valid scheduled date and time appear in the calendar.



\---



\# 10. Manage Drafts



Choose:



```text

7\. Manage Drafts

```



Select an existing draft.



Available management actions include:



```text

1\. Change Scheduled Date/Time

2\. Unschedule

3\. Delete

4\. Return

```



NEORUINS checks for exact scheduling conflicts.



It also warns when scheduled Posts are less than 60 minutes apart.



A frequency warning does not automatically prevent scheduling, but an exact schedule conflict is rejected.



\---



\# 11. Scheduling Format



When NEORUINS asks for a scheduled date and time, use:



```text

YYYY-MM-DD HH:MM

```



Example:



```text

2026-10-15 18:00

```



The scheduled time must be in the future.



Press Enter when the workflow allows it if you do not want to schedule the draft.



\---



\# 12. Track Post Performance



Choose:



```text

8\. Track Post Performance

```



NEORUINS loads approved Posts and allows you to select one for performance tracking.



If the selected Post has a matching X publication record and X Post ID, NEORUINS offers:



```text

1\. Retrieve Live Metrics from X

2\. Enter Metrics Manually

0\. Cancel

```



\## Live X Metrics



When live retrieval is selected, NEORUINS requests available metrics through the X API.



Depending on X API availability and permissions, retrieved information may include:



\- Likes

\- Reposts

\- Replies

\- Bookmarks

\- Views

\- Quote Posts

\- X engagements

\- Profile clicks

\- Publication time



NEORUINS asks for confirmation before saving retrieved metrics.



Live records are marked:



```text

Data Source: X API

```



\## Manual Performance Tracking



Metrics can also be entered manually.



The manual workflow accepts:



\- Likes

\- Reposts

\- Replies

\- Bookmarks

\- Views



Manual records are marked:



```text

Data Source: Manual Entry

```



Type:



```text

CANCEL

```



at supported manual tracking prompts to stop without saving the record.



Performance data is stored in:



```text

performance\_history.txt

```



\---



\# 13. Performance Score



NEORUINS calculates a local performance score using engagement activity relative to views.



The current scoring system gives additional weight to:



\- Reposts

\- Replies

\- Bookmarks



The score is capped at:



```text

100

```



This score is an internal NEORUINS measurement.



It should not be interpreted as an official X score or a guarantee of future performance.



Small-view Posts can produce unusually high scores, so performance should be interpreted together with views, engagement counts, and sample size.



\---



\# 14. View Performance History



Choose:



```text

9\. View Performance History

```



This displays stored performance records from:



```text

performance\_history.txt

```



The history can contain both manually entered records and records retrieved through the X API.



\---



\# 15. Performance Analytics



Choose:



```text

10\. Performance Analytics

```



This provides overall statistics across stored performance records.



NEORUINS calculates information such as:



\- Number of tracked Posts

\- Average views

\- Average likes

\- Average reposts

\- Average replies

\- Average bookmarks

\- Average performance score



It also displays the Post with the highest stored performance score.



\---



\# 16. Post Type Analytics



Choose:



```text

11\. Post Type Analytics

```



This groups performance records by content type:



```text

Gaming Question

Hot Take

News Reaction

Streaming Post

Meme Style

```



For each type with available data, NEORUINS calculates average performance measurements.



This can help creators observe how different content formats perform over time.



\---



\# 17. Performance Insights



Choose:



```text

12\. Performance Insights

```



This is the real-data recommendation layer introduced for NEORUINS v1.0.0.



For recommendations, NEORUINS distinguishes records retrieved from the X API from older or manually entered records.



The system reports:



\- Total stored performance records

\- Real X API records used

\- Legacy/manual records excluded from recommendations

\- Average real-X performance measurements

\- Sample-size confidence

\- Real-X data by Post type

\- Data-based guidance

\- Recent-versus-earlier comparisons when enough data exists



NEORUINS deliberately limits strong recommendations when the real-X sample is small.



This helps prevent a few early Posts from being treated as a reliable long-term strategy.



\---



\# 18. Posting Time Analytics



Choose:



```text

13\. Posting Time Analytics

```



This analyzes tracked Posts according to their actual publication time.



Time periods include:



```text

Morning

Midday

Afternoon

Evening

Night

```



NEORUINS compares available performance measurements within these periods.



Several Posts should be collected before treating differences as meaningful patterns.



\---



\# 19. Posting Hour Analytics



Choose:



```text

14\. Posting Hour Analytics

```



This groups tracked Posts according to the exact hour in which they were published.



For hours containing data, NEORUINS can display measurements such as:



\- Posts tracked

\- Average views

\- Average likes

\- Average reposts

\- Average replies

\- Average performance score



This is a measurement tool rather than a guarantee that a specific hour will perform well in the future.



\---



\# 20. Posting Hour Insights



Choose:



```text

15\. Posting Hour Insights

```



This looks for posting-hour patterns after enough observations have been collected.



NEORUINS requires at least three tracked Posts at the same publication hour before that hour is used for an hour insight.



The resulting information should be treated as a testing signal rather than a guarantee.



\---



\# 21. Posting Day Analytics



Choose:



```text

16\. Posting Day Analytics

```



This groups performance records according to the day of the week when the Post was published.



NEORUINS can compare performance across:



```text

Monday

Tuesday

Wednesday

Thursday

Friday

Saturday

Sunday

```



Only days with tracked publication data are analyzed.



\---



\# 22. Posting Day Insights



Choose:



```text

17\. Posting Day Insights

```



This uses accumulated performance information to identify patterns associated with publication days.



The usefulness of these insights increases as more Posts are tracked.



Avoid making major scheduling decisions from very small samples.



\---



\# 23. Posting Schedule Insights



Choose:



```text

18\. Posting Schedule Insights

```



This combines publication timing information to provide schedule-oriented observations.



The purpose is to help creators test posting schedules using their own collected performance data rather than relying only on generic social-media advice.



Continue collecting data before treating an observed pattern as established.



\---



\# 24. Content Strategy Insights



Choose:



```text

19\. Content Strategy Insights

```



This analyzes stored performance information from a content-strategy perspective.



It is designed to help identify useful patterns in how different types of content have performed.



These insights are based on the data available to NEORUINS and should be treated as evidence for further testing rather than guaranteed outcomes.



\---



\# 25. Content Type + Schedule Insights



Choose:



```text

20\. Content Type + Schedule Insights

```



This combines content-type information with scheduling information.



The feature is intended to help investigate questions such as whether a particular type of gaming content performs differently depending on when it is published.



Meaningful conclusions require enough observations across content types and posting times.



\---



\# 26. X Publishing Layer



Choose:



```text

21\. X Publishing Layer

```



The publishing menu contains:



```text

1\. Publish an Approved Post

2\. Review Due Scheduled Posts

0\. Return

```



This is the section of NEORUINS that communicates with X for publishing.



A correctly configured `.env` file and appropriate X API access are required.



\---



\# 27. Publishing an Approved Post



Inside the X Publishing Layer, choose:



```text

1\. Publish an Approved Post

```



NEORUINS allows you to select an approved Post.



Before publishing, review the content carefully.



NEORUINS uses a confirmation step before sending the Post to X.



After successful publication, NEORUINS records publication information locally, including the X Post ID when available.



Published records are stored in:



```text

published\_posts.txt

```



The publication record can later connect that Post to live X performance tracking.



\---



\# 28. Due Scheduled Posts



Inside the X Publishing Layer, choose:



```text

2\. Review Due Scheduled Posts

```



NEORUINS checks scheduled drafts whose scheduled time has arrived or passed.



Due Posts are presented for human review.



The intended workflow is:



```text

Draft

&#x20;  ↓

Schedule

&#x20;  ↓

Post Becomes Due

&#x20;  ↓

Review

&#x20;  ↓

Confirm

&#x20;  ↓

Publish to X

```



A scheduled time does not by itself authorize silent publication.



The user remains responsible for confirming the supported publishing action.



After successful publication, the published Post is recorded and the corresponding scheduled draft is removed from the active draft list.



\---



\# 29. Startup Schedule Check



When NEORUINS starts, it checks whether scheduled Posts are currently due for review.



If nothing is due, it reports that no scheduled Posts are due.



If Posts are due, NEORUINS alerts you so they can be reviewed through the publishing workflow.



The startup check is an alert.



It does not silently publish the content.



\---



\# 30. Published Post Records



Successful X publications are recorded in:



```text

published\_posts.txt

```



Publication records allow NEORUINS to associate approved content with information such as:



\- X Post ID

\- Connected account

\- Publication time

\- Post text



This information supports later performance tracking.



\---



\# 31. Local Data Files



NEORUINS v1.0.0 uses several local text files:



```text

approved\_posts.txt

content\_history.txt

drafts.txt

performance\_history.txt

published\_posts.txt

```



These files are created or updated as relevant features are used.



They are intentionally excluded from the public Git repository.



Back up important local data before deleting or replacing these files.



\---



\# 32. X API Credentials



NEORUINS loads X credentials from:



```text

.env

```



Required variables are:



```text

X\_API\_KEY=

X\_API\_KEY\_SECRET=

X\_ACCESS\_TOKEN=

X\_ACCESS\_TOKEN\_SECRET=

```



Never enter your credentials directly into `main.py`.



Never upload `.env` to GitHub.



See:



```text

docs/X\_API\_SETUP.md

```



for setup instructions.



\---



\# 33. Safe Publishing Practices



Before publishing:



1\. Read the entire Post.

2\. Verify the correct X account is connected.

3\. Check spelling and context.

4\. Confirm that the content is appropriate for your audience.

5\. Confirm publication only when you actually want the Post to go live.



NEORUINS is intended to assist the creator, not replace creator judgment.



\---



\# 34. Analytics and Sample Size



Analytics become more useful as more real performance data is collected.



A small number of Posts can produce misleading averages.



NEORUINS includes several safeguards and informational messages intended to discourage overinterpreting limited samples.



Creators should use analytics to:



\- Observe

\- Test

\- Compare

\- Collect more data

\- Refine future experiments



Do not assume an observed pattern guarantees future reach or engagement.



\---



\# 35. Exiting NEORUINS



Choose:



```text

22\. Exit

```



NEORUINS shuts down and returns you to PowerShell.



\---



\# 36. Recommended Beginner Workflow



A simple first workflow is:



```text

Start NEORUINS

&#x20;     ↓

Generate New Post

&#x20;     ↓

Choose a Content Type

&#x20;     ↓

Review the Generated Variations

&#x20;     ↓

Edit if Necessary

&#x20;     ↓

Approve or Save as Draft

&#x20;     ↓

Schedule if Desired

&#x20;     ↓

Review Before Publishing

&#x20;     ↓

Publish Through the X Publishing Layer

&#x20;     ↓

Wait for Performance Data

&#x20;     ↓

Track Metrics

&#x20;     ↓

Review Analytics and Insights

&#x20;     ↓

Use the Data to Guide Future Tests

```



\---



\# 37. Troubleshooting



\## NEORUINS Will Not Start



Confirm Python is available:



```powershell

py -V:3.12 --version

```



Install dependencies:



```powershell

py -m pip install -r requirements.txt

```



Then try:



```powershell

py -V:3.12 main.py

```



\## X Authentication Fails



Check:



```text

docs/X\_API\_SETUP.md

```



Verify that `.env` exists and contains all four required credentials.



Do not share the contents of `.env` while requesting help.



\## No Analytics Are Available



Performance analytics require stored performance records.



Track published Posts using:



```text

8\. Track Post Performance

```



\## No Live X Metrics Option Appears



The selected approved Post must have a matching publication record containing an X Post ID.



Posts that were never published through a recorded NEORUINS workflow may require manual performance tracking.



\## No Scheduled Posts Appear



Confirm that the draft has a valid scheduled date and time.



Use:



```text

6\. Content Calendar

```



to inspect scheduled content.



\---



\# 38. Additional Documentation



See:



```text

README.md

LICENSE.md

SECURITY.md

CONTRIBUTING.md

CHANGELOG.md

ROADMAP.md

docs/INSTALLATION.md

docs/CONFIGURATION.md

docs/X\_API\_SETUP.md

```



for additional information.



\---



\# NEORUINS Creator Edition



Version 1.0.0



Copyright © 2026 Angelo Padula



All rights reserved.
