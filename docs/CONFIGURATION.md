\# NEORUINS Configuration Guide



This guide explains the local configuration used by NEORUINS Creator Edition v1.0.0.



\## Environment Configuration



NEORUINS uses environment variables to keep X API credentials separate from the application source code.



The repository includes:



```text

.env.example

```



This file contains empty placeholders and is safe to include in the public repository.



Your local installation uses:



```text

.env

```



The `.env` file contains your private credentials and must never be committed to Git or uploaded publicly.



\## Creating `.env`



From the NEORUINS project directory, run:



```powershell

Copy-Item .env.example .env

```



Then open `.env` in a text editor.



\## X API Variables



NEORUINS expects these environment variables:



```text

X\_API\_KEY=

X\_API\_KEY\_SECRET=

X\_ACCESS\_TOKEN=

X\_ACCESS\_TOKEN\_SECRET=

```



Enter the credentials issued for your own X Developer application.



Do not add quotation marks unless your environment specifically requires them.



\## Example



Your `.env.example` should remain:



```text

X\_API\_KEY=

X\_API\_KEY\_SECRET=



X\_ACCESS\_TOKEN=

X\_ACCESS\_TOKEN\_SECRET=

```



Your real `.env` will contain your credentials locally.



Never copy the contents of your real `.env` into documentation, screenshots, issues, commits, or messages.



\## Local Runtime Data



NEORUINS may use the following local files while the application is running:



```text

approved\_posts.txt

content\_history.txt

drafts.txt

performance\_history.txt

published\_posts.txt

```



These files contain local application data and are excluded from the public repository by `.gitignore`.



Depending on the features you use, NEORUINS may create or update these files during normal operation.



\## Git Protection



The project's `.gitignore` excludes sensitive or machine-specific content, including:



```text

.env

\_\_pycache\_\_/

approved\_posts.txt

content\_history.txt

drafts.txt

performance\_history.txt

published\_posts.txt

backups/

local\_data\_backup/

\*.log

.vscode/

.idea/

```



Do not remove `.env` from `.gitignore`.



\## X API Setup



X Developer configuration is covered separately in:



```text

docs/X\_API\_SETUP.md

```



X API requirements, permissions, features, and pricing may change over time. Always verify current requirements through official X Developer documentation.



\## Security



If you accidentally expose an API key or access token, treat the credential as compromised and revoke or regenerate it through the appropriate X Developer account controls.



See:



```text

SECURITY.md

```



for additional security guidance.



\## Application Configuration



NEORUINS Creator Edition v1.0.0 is primarily configured through its source code, local runtime files, and environment variables.



Future versions may introduce dedicated configuration files or a graphical configuration interface.
