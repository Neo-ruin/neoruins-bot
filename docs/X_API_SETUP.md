\# NEORUINS X API Setup Guide



This guide explains how to connect your own X account to NEORUINS Creator Edition v1.0.0.



NEORUINS uses the X API for publishing Posts and retrieving performance information.



> Important: X Developer features, access requirements, pricing, permissions, and interfaces can change. Always check the current official X Developer documentation before purchasing API access or changing your application configuration.



\---



\## 1. Create an X Developer Account



You need access to the X Developer platform before NEORUINS can communicate with the X API.



Use your own X account when registering.



Follow the current instructions provided by X for creating or accessing a developer account.



Official documentation:



https://docs.x.com/



\---



\## 2. Create or Select a Developer App



Inside the X Developer Console, create or select the application that NEORUINS will use.



Your application provides the credentials that allow NEORUINS to authenticate with the X API.



Never use another person's API credentials.



\---



\## 3. Configure User Authentication



NEORUINS Creator Edition v1.0.0 uses OAuth 1.0a user authentication through Tweepy.



The application requires credentials for the X account that will be connected to NEORUINS.



For publishing functionality, configure the X application with the permissions necessary to read account information and publish Posts.



NEORUINS should not be given permissions that are unnecessary for its intended features.



\---



\## 4. Generate Your Credentials



NEORUINS expects four credential values:



```text

API Key

API Key Secret

Access Token

Access Token Secret

```



These correspond to the following environment variables:



```text

X\_API\_KEY=

X\_API\_KEY\_SECRET=

X\_ACCESS\_TOKEN=

X\_ACCESS\_TOKEN\_SECRET=

```



Generate credentials through the current X Developer application controls.



If you change application permissions after generating access credentials, you may need to regenerate the affected credentials.



\---



\## 5. Create Your Local `.env`



NEORUINS includes:



```text

.env.example

```



Create your private local configuration:



```powershell

Copy-Item .env.example .env

```



Open `.env` and enter your own credentials:



```text

X\_API\_KEY=YOUR\_API\_KEY

X\_API\_KEY\_SECRET=YOUR\_API\_KEY\_SECRET



X\_ACCESS\_TOKEN=YOUR\_ACCESS\_TOKEN

X\_ACCESS\_TOKEN\_SECRET=YOUR\_ACCESS\_TOKEN\_SECRET

```



Replace each example value with the credential issued to your application.



Do not include the words `YOUR\_API\_KEY`, `YOUR\_API\_KEY\_SECRET`, `YOUR\_ACCESS\_TOKEN`, or `YOUR\_ACCESS\_TOKEN\_SECRET` in the finished configuration.



\---



\## 6. Protect Your Credentials



Your `.env` file is private.



Never upload it to GitHub.



Never place real credentials in:



\- `.env.example`

\- README files

\- Documentation

\- Source code

\- Screenshots

\- GitHub issues

\- Pull requests

\- Chat messages

\- Public forums



The NEORUINS `.gitignore` file excludes `.env` by default.



Do not remove this protection.



\---



\## 7. Install the X Integration Dependencies



From the NEORUINS project directory, run:



```powershell

py -m pip install -r requirements.txt

```



NEORUINS v1.0.0 uses:



```text

tweepy

python-dotenv

```



Tweepy provides the Python interface used by NEORUINS to communicate with the X API.



`python-dotenv` loads the private credentials from your local `.env` file.



\---



\## 8. Start NEORUINS



Run:



```powershell

py -V:3.12 main.py

```



NEORUINS will load the credentials from `.env` when X functionality is used.



Do not paste credentials into the NEORUINS menu.



\---



\## 9. Publishing Workflow



NEORUINS Creator Edition v1.0.0 uses a human-controlled publishing workflow.



The intended workflow is:



```text

Generate

&#x20;  ↓

Review

&#x20;  ↓

Approve

&#x20;  ↓

Schedule or Select

&#x20;  ↓

Review for Publishing

&#x20;  ↓

Confirm

&#x20;  ↓

Publish to X

```



NEORUINS does not require you to surrender control of what gets published.



Review every Post before confirming publication.



\---



\## 10. Scheduled Posts



Scheduling a Post inside NEORUINS does not mean the application should silently publish it without review.



When a scheduled Post becomes due, NEORUINS can surface it for review.



The user confirms publication before the supported publishing workflow sends it to X.



\---



\## 11. Performance Metrics



NEORUINS can retrieve available X performance information for published Posts.



Depending on API availability and permissions, metrics used by NEORUINS may include:



\- Views

\- Likes

\- Reposts

\- Replies

\- Bookmarks

\- Engagement information



Metric availability can depend on the X API endpoint, authentication context, account, and current X API capabilities.



NEORUINS separates records retrieved from the X API from older or manually entered performance records when generating its real-data recommendations.



\---



\## 12. API Usage and Costs



X API access, usage limits, and pricing are controlled by X and may change independently of NEORUINS.



NEORUINS does not provide X API access itself.



Before using publishing or analytics features:



1\. Review the current X API access options.

2\. Review applicable usage limits.

3\. Review current pricing or credit requirements.

4\. Monitor your own API usage.



Do not rely on old screenshots, tutorials, or pricing information when making purchasing decisions.



\---



\## 13. Troubleshooting Authentication



If authentication fails, check:



1\. `.env` exists in the NEORUINS project folder.

2\. All four required values are present.

3\. No credential was accidentally copied incorrectly.

4\. Your X Developer application is active.

5\. The application has the permissions required for the action.

6\. The Access Token belongs to the account you intend to connect.

7\. Credentials were regenerated if required after permission changes.



Never post your credentials publicly while requesting support.



\---



\## 14. If a Credential Is Exposed



Treat an exposed API key, secret, access token, or access-token secret as compromised.



Use the current X Developer controls to revoke or regenerate the affected credential.



Then update your local `.env`.



Remember that deleting a secret from the latest Git commit does not necessarily remove it from earlier Git history.



See:



```text

SECURITY.md

```



for additional security guidance.



\---



\## 15. Current X Documentation



Because the X API evolves independently of NEORUINS, use the official X documentation as the authoritative source for current API requirements:



https://docs.x.com/



NEORUINS documentation describes the integration used by Creator Edition v1.0.0 but does not replace official X Developer documentation.
