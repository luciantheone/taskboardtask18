# Sources

All pages were read on 21 Oct 2026. "Official" means a Redbelly, Averer or DAO page. IDs match the guide.

## Source list

| ID | Page | Link | Kind |
| --- | --- | --- | --- |
| S1 | Redbelly Developer Portal, User access | https://vine.redbelly.network/identity/user-access/ | Official |
| S2 | Redbelly Developer Portal, Identity and participation | https://vine.redbelly.network/identity/ | Official |
| S3 | Redbelly Developer Portal, Accredited issuers | https://vine.redbelly.network/identity/accredited-issuers/ | Official |
| S4 | Redbelly Network Terms and Conditions, clause 15 | https://redbelly.network/terms-and-conditions | Official |
| S5 | Redbelly Developer Portal, Staking | https://vine.redbelly.network/nodes/staking/ | Official |
| S6 | Redbelly Developer Portal, Native currency | https://vine.redbelly.network/native-currency/ | Official |
| S7 | Redbelly Developer Portal, Bridged tokens, Lucid Labs | https://vine.redbelly.network/bridged-tokens/lucidlabs/ | Official |
| S8 | Redbelly Developer Portal, Environments | https://vine.redbelly.network/environments | Official |
| S9 | Redbelly Technical Documentation, Individual onboarding overview | https://docs.redbelly.network/pages/eligibility-sdk/onboarding/individual/overview/ | Official |
| S10 | Redbelly Access portal. Wording read from its own script files, see the evidence page (/evidence) for file names and SHA-256 checksums | https://access.redbelly.network/ | Official |
| S11 | Snapshot vote "DAO Proposal: Increase Governance Accessibility and Protect Contributor Privacy" (rbnt.eth), passed, ended 5 July 2026 | https://snapshot.box/#/s:rbnt.eth/proposal/0xa57ccc9a6d554c9e5a1b1ca429ad2affc2e9058f12ea50bce999460f2aea4e02 | Official, DAO |
| S12 | Averer help centre | https://averer-help.freshdesk.com/support/home | Official |
| S13 | Averer help centre, Submit a ticket (form fields read 21 Oct 2026) | https://averer-help.freshdesk.com/support/tickets/new | Official |
| S14 | Redbelly Developer Portal, Support | https://vine.redbelly.network/support/ | Official |
| S15 | Redbelly Developer Portal, Eligibility | https://vine.redbelly.network/identity/eligibility/ | Official |

## Claim map

| Claim in the guide | Source | Status |
| --- | --- | --- |
| Every participant must prove identity before access | S2 | Official |
| A user claims an access credential from an accredited issuer, then self enables write access | S1, S2 | Official |
| The credential needs a valid passport with biometric checks | S1, S3 | Official |
| Onboarding covers wallet authentication, KYC verification and on chain permission setup | S9 | Official |
| Issuers verify submitted documents and issue credentials | S15 | Official |
| Redbelly Access is the portal, Averer is the issuer | S1, S10 | Official |
| MetaMask and Coinbase Wallet are the wallets the portal names | S10 | Official, portal FAQ |
| The issuer covers the fees to grant network access | S10 | Official, portal FAQ |
| Pending checks take a few minutes, rarely a few days | S10 | Official, portal message |
| Incomplete means resubmit, failed means contact Averer, with the button names | S10 | Official, portal messages |
| 10 accounts per identity, and the message "Account allocation exhausted." | S10 | Official, portal code and message |
| Add another account and Link another wallet buttons, and the accountability warning | S10 | Official, portal |
| Button names in Part C and D | S10 | Official, portal |
| Mainnet name, RPC URL, chain ID 151, symbol RBNT, block explorer | S8 | Official |
| RBNT is native, with exchange listings on Gate and MEXC | S6 | Official |
| WRBNT exists on Redbelly, Ethereum and Base, bridged through Lucid Labs | S7 | Official |
| Holding RBNT on an exchange needs no Redbelly KYC | S1, S6 | Derived: access gates write access on Redbelly Network, and nothing is signed there |
| Holding WRBNT on Ethereum or Base needs no Redbelly KYC | S1, S7 | Derived, same reasoning |
| Bridging out of mainnet needs KYC | S1, S7 | Derived: it is a transaction signed on Redbelly |
| Bridging into mainnet | S7 | Unconfirmed: the page does not mention KYC or enablement |
| Staking needs KYC | S5, S1 | Derived: staking is a deposit call on a mainnet contract, and write access needs an enabled account. The staking page does not use the word KYC |
| A node stakes 100,000 RBNT | S5 | Official |
| A DAO vote removed geographic restrictions for general DAO members and kept them for High Council members and General DAO Leadership, ended 5 July 2026 | S11 | Official, DAO vote (Passed) |
| 18 jurisdictions where Redbelly does not offer services | S4 clause 15.1 | Official |
| Tax residents of or people located there may not use the website, platform or tools | S4 clause 15.2 | Official |
| Embargo and prohibited party representations | S4 clause 15.3 | Official |
| What happens past 10 accounts, beyond the portal message | None | Not described in the sources |
| Difference between Add another account and Link another wallet | None | Not explained by the portal text read |
| Averer ticket form fields: Full Name, Email Address, Subject, What is your issue?, Redbelly Wallet Address, Attach files, reCAPTCHA | S13 | Official |
| Discord for questions about the network | S14 | Official |

## Advice that is not a fact

- Type the portal address yourself instead of following a link in a message.
- Enable your wallet before bridging in.
- What to put in a ticket: the exact words on the screen, the date, the wallet address.

## Not covered

The portal screens were not captured as screenshots. The portal wording comes from its script files, listed with checksums in the evidence page (/evidence). File names change when the portal is redeployed, so check against the live portal before you publish again.

An earlier build of this guide is kept in `archive/earlier-build/`. It is not part of this submission.
