#!/usr/bin/env bash
set -euo pipefail

apply=0
gemini_home="${GEMINI_HOME:-$HOME/.gemini}"

while (($#)); do
  case "$1" in
    --apply) apply=1 ;;
    --dry-run) apply=0 ;;
    --gemini-home)
      shift
      gemini_home="${1:?missing --gemini-home value}"
      ;;
    -h|--help)
      printf '%s\n' "usage: scripts/install_system_gemini.sh [--dry-run|--apply] [--gemini-home PATH]"
      exit 0
      ;;
    *)
      printf 'unknown argument: %s\n' "$1" >&2
      exit 2
      ;;
  esac
  shift
done

# Verify required CLI binary is on PATH before any non-dry-run work
if [[ "$apply" -eq 1 ]]; then
  if ! command -v agy >/dev/null 2>&1; then
    printf "error: Antigravity CLI requires the managed 'agy' CLI on PATH.\n" >&2
    printf 'Run github-device-sync/modules/macos-ubuntu-bootstrap; remote installer streams are unsupported.\n' >&2
    exit 1
  fi
  # Clean up legacy rldyour-gemini extension (renamed in 1.4.0 to rldyour-antigravity-cli)
  if [[ -d "$gemini_home/extensions/rldyour-gemini" ]]; then
    printf 'cleanup: removing legacy rldyour-gemini extension directory\n'
    rm -rf "$gemini_home/extensions/rldyour-gemini"
  fi
fi

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
extension_dir="$gemini_home/extensions/rldyour-antigravity-cli"

if [[ "$apply" -eq 0 ]]; then
  printf 'dry-run: would install Antigravity CLI extension into %s\n' "$extension_dir"
  printf 'dry-run: would copy GEMINI.md, gemini-extension.json, commands, skills, agents, hooks, and policies\n'
  printf 'dry-run: would also install Antigravity CLI settings and MCP config\n'
  exit 0
fi

mkdir -p "$extension_dir"
cp "$repo_root/GEMINI.md" "$extension_dir/GEMINI.md"
cp "$repo_root/gemini-extension.json" "$extension_dir/gemini-extension.json"
rm -rf "$extension_dir/commands" "$extension_dir/skills" "$extension_dir/agents" "$extension_dir/hooks" "$extension_dir/policies"
cp -R "$repo_root/.gemini/commands" "$extension_dir/commands"
cp -R "$repo_root/.gemini/skills" "$extension_dir/skills"
cp -R "$repo_root/.gemini/agents" "$extension_dir/agents"
cp -R "$repo_root/.gemini/hooks" "$extension_dir/hooks"
cp -R "$repo_root/.gemini/policies" "$extension_dir/policies"

mkdir -p "$gemini_home/antigravity-cli"
cp "$repo_root/.gemini/antigravity-cli/settings.json" "$gemini_home/antigravity-cli/settings.json"
cp "$repo_root/.gemini/antigravity-cli/mcp_config.json" "$gemini_home/antigravity-cli/mcp_config.json"
printf 'installed: %s (antigravity runtime)\n' "$extension_dir"
