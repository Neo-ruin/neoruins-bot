\# NEORUINS Installation Guide



This guide explains how to install NEORUINS Creator Edition on Windows.



\## Requirements



Before installing NEORUINS, you will need:



\- Windows 10 or Windows 11

\- Python 3.12 or newer

\- Internet access for X API features

\- An X Developer account for publishing and metrics features



\## 1. Download NEORUINS



Download or clone the NEORUINS repository to your computer.



If using Git:



```powershell

git clone YOUR\_REPOSITORY\_URL

cd neoruins-bot

```



The final repository URL will be added after the public GitHub repository is created.



\## 2. Verify Python



Open PowerShell inside the NEORUINS project folder and run:



```powershell

py --version

```



You should see a Python version of 3.12 or newer.



On Windows systems with multiple Python versions installed, you can select Python 3.12 explicitly:



```powershell

py -V:3.12 --version

```



\## 3. Install Dependencies



Install the required Python packages:



```powershell

py -m pip install -r requirements.txt

```



NEORUINS v1.0.0 requires:



\- Tweepy

\- python-dotenv



\## 4. Create Your Environment File



NEORUINS includes a safe configuration template named:



```text

.env.example

```



Create a local `.env` file from the template.



In PowerShell:



```powershell

Copy-Item .env.example .env

```



Do not publish or commit your `.env` file.



\## 5. Configure X API Credentials



Open `.env` and enter your own X Developer API credentials:



```text

X\_API\_KEY=

X\_API\_KEY\_SECRET=

X\_ACCESS\_TOKEN=

X\_ACCESS\_TOKEN\_SECRET=

```



Never share these values publicly.



Detailed X API configuration instructions are provided separately in:



```text

docs/X\_API\_SETUP.md

```



\## 6. Start NEORUINS



Run:



```powershell

py -V:3.12 main.py

```



If Python 3.12 is your default Python installation, you may also use:



```powershell

py main.py

```



\## 7. First Launch



NEORUINS should display its interactive main menu.



Local runtime files may be created as you use features such as:



\- Draft management

\- Approved posts

\- Content history

\- Performance tracking

\- Published post tracking



These local runtime files are excluded from the public repository through `.gitignore`.



\## Security



Before connecting an X account, read:



```text

SECURITY.md

```



Never place real credentials in:



\- `.env.example`

\- Documentation

\- Screenshots

\- GitHub issues

\- Source code

\- Public repositories



\## Next Steps



After installation:



1\. Configure your X API credentials.

2\. Start NEORUINS.

3\. Generate and review content.

4\. Learn the scheduling workflow.

5\. Test X integration carefully before publishing production content.



See the NEORUINS User Guide for detailed usage instructions.
