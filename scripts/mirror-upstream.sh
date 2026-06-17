#!/usr/bin/env bash
#
# Mirror all branches and tags from an upstream repository into a downstream
# repository under the phenotype org. Re-run idempotently to keep the mirror
# in sync with upstream.
#
# Usage:
#   scripts/mirror-upstream.sh <upstream-repo> <downstream-repo> [--prune]
#
# Example:
#   scripts/mirror-upstream.sh mark3labs/mcp-go phenotype/mcp-go
#
# Environment:
#   GIT_AUTHOR_NAME, GIT_AUTHOR_EMAIL, GIT_COMMITTER_NAME, GIT_COMMITTER_EMAIL
#       Optional. Used when git itself needs an identity to perform the mirror.
#       Authentication is taken from the existing git credential helper / config.
#
# Notes:
#   * Both repos must already exist on the remote.
#   * Refspec mirrors all refs (refs/heads/*, refs/tags/*, refs/pull/*/head).
#   * Without --prune, refs deleted upstream are NOT removed downstream; pass
#     --prune to make the mirror an exact replica.

set -euo pipefail

if [[ $# -lt 2 || $# -gt 3 ]]; then
    echo "usage: $0 <upstream-repo> <downstream-repo> [--prune]" >&2
    exit 2
fi

UPSTREAM="$1"
DOWNSTREAM="$2"
PRUNE_FLAG=""
if [[ "${3:-}" == "--prune" ]]; then
    PRUNE_FLAG="--prune"
fi

if ! command -v git >/dev/null 2>&1; then
    echo "error: git is required" >&2
    exit 1
fi

if ! git remote get-url origin >/dev/null 2>&1; then
    echo "error: no 'origin' remote configured in $(pwd)" >&2
    exit 1
fi

REMOTE_URL="$(git remote get-url origin)"
case "$REMOTE_URL" in
    *"$DOWNSTREAM"*) ;;
    *) echo "warning: origin ($REMOTE_URL) does not match downstream $DOWNSTREAM" >&2 ;;
esac

echo "Fetching refs from upstream: $UPSTREAM"
git fetch "https://github.com/${UPSTREAM}.git" \
    '+refs/heads/*:refs/heads/*' \
    '+refs/tags/*:refs/tags/*' \
    '+refs/pull/*/head:refs/pull/*/head' \
    $PRUNE_FLAG

echo "Pushing mirror to downstream: $DOWNSTREAM"
git push "https://github.com/${DOWNSTREAM}.git" \
    'refs/heads/*:refs/heads/*' \
    'refs/tags/*:refs/tags/*' \
    'refs/pull/*/head:refs/pull/*/head' \
    $PRUNE_FLAG

echo "Mirror complete: $UPSTREAM -> $DOWNSTREAM"
