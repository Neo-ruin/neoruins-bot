\# NEORUINS Security Policy



NEORUINS connects to the X API and requires users to manage their own API credentials securely.



\## Credential Security



Never commit or publish your `.env` file.



NEORUINS expects X API credentials to be stored locally using the following environment variables:



\- `X\_API\_KEY`

\- `X\_API\_KEY\_SECRET`

\- `X\_ACCESS\_TOKEN`

\- `X\_ACCESS\_TOKEN\_SECRET`



Use `.env.example` as the configuration template.



Your real credentials belong only in your local `.env` file.



\## Never Share Credentials



Do not share API keys, access tokens, secrets, passwords, or other authentication credentials in:



\- GitHub repositories

\- Issues

\- Pull requests

\- Screenshots

\- Documentation

\- Public messages



\## Exposed Credentials



If credentials are accidentally exposed, treat them as compromised.



Revoke or regenerate the affected credentials through the appropriate X Developer account controls and update your local `.env` file.



Removing a secret from the latest Git commit does not necessarily remove it from previous Git history.



\## Publishing Safety



NEORUINS v1.0.0 uses human confirmation before publishing through its supported publishing workflow.



Users should review content before confirming publication.



\## Reporting a Security Issue



Do not publicly disclose security vulnerabilities that could expose credentials or compromise user accounts.



Please report security concerns privately to the project owner.



A dedicated security contact method may be added in a future release.



\## Supported Version



Security updates currently target the latest NEORUINS Creator Edition release.



| Version | Supported |

| --- | --- |

| 1.0.x | Yes |

| Earlier development builds | No |



\## Disclaimer



Users are responsible for protecting their own API credentials, X Developer accounts, and connected X accounts.



See `LICENSE.md` for the software warranty and liability terms.
