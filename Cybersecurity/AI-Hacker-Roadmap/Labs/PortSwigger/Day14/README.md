# Evidence — Unprotected admin functionality

## Scope

This evidence package covers only the completed `Unprotected admin functionality` lab in PortSwigger Web Security Academy. The temporary lab domain and all session values are omitted.

## Objective

Record the evidence that an administration function in this official lab was reachable without administrator credentials after following a public hint.

## Baseline

No administrator credentials were used, and the management function was not visible in normal navigation. The original notes do not contain a baseline HTTP status, so no status is guessed.

## Single Change

The request target changed from the public `/robots.txt` hint to the hinted `/administrator-panel` path. The test remained within the same official lab and did not add administrator credentials.

## Observed Result

The management page returned status `200` and showed the lab user list and Delete operation. Completing the lab objective displayed `User deleted successfully!`; the lab status displayed `Solved`.

## Why This Evidence Supports the Finding

The redacted request summary, response summary, and solved screenshot form one evidence chain: a public hint named the management path, the path returned the management page without administrator credentials, and the official lab recorded the specified action as solved.

## Redactions

The temporary lab domain, instance identifier, Cookie and Session values, Authorization values, full request/response headers, and any unnecessary tracking values are not included. The screenshot uses opaque redaction over the address-bar instance domain and tab identifier.

## Limitations

This package documents one completed official lab only. It does not contain server source code, a full baseline HTTP response, or evidence about another application. It therefore cannot support conclusions about real websites.
