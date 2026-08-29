# Evidence — Information disclosure in error messages

## Scope

This evidence package covers only the completed `Information disclosure in error messages` lab in PortSwigger Web Security Academy. The temporary Lab domain and all session data are omitted.

## Objective

Determine the third-party framework version disclosed by the Lab's verbose error behavior, then submit the version as the official Lab answer.

## Baseline

`GET /product?productId=1` visibly displayed a normal product detail page for `3D Voice Assistants`.

## Single Change

Only `productId` was changed from `1` to ordinary non-numeric text `abc`.

## Observed Result

The browser environment blocked the changed navigation with `ERR_BLOCKED_BY_CLIENT` before it reached the Lab. Therefore, no direct server error response is claimed in this evidence package. The official Lab Solution was then consulted; it identifies the disclosed framework version as `Apache Struts 2 2.3.31`. The learner confirmed the Lab subsequently displayed `Solved` after submitting the official answer.

## Why This Evidence Supports the Finding

The baseline and single-variable change establish the intended test boundary. The official Lab Solution supplies the documented error-message result and version after the browser client prevented direct observation. The completion confirmation establishes that the submitted version satisfied the official Lab.

## Root Cause

The Lab's intended behavior is that a detailed error response exposes a third-party framework version when an unexpected parameter type causes an exception. Detailed implementation errors should not be returned to ordinary users because version information can aid further analysis. This package does not contain server source code, so it does not assert more specific internal implementation details.

## Recommended Remediation

- Return a generic error message to ordinary users instead of stack traces, framework versions or internal exception details.
- Record detailed exceptions in server-side logs with access restricted to authorized operators.
- Use centralized error handling so accidental exceptions do not expose internal details.
- Keep third-party frameworks updated and monitor their supported versions.

## Redactions

Temporary Lab domain, instance ID, Cookie, Session, Authorization values, complete request/response headers, and the full error stack trace are not included.

## Limitations

This package documents one official training Lab. The changed request was blocked by the browser client, so no direct server error response was captured in this session. The framework version and error behavior are therefore attributed to the official Lab Solution, while `Solved` is recorded from the learner's confirmation. Nothing here supports a conclusion about a real website.
