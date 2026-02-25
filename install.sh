#!/usr/bin/env bash
set -euo pipefail

REPO_URL="https://github.com/ZhanlinCui/Ultimate-Agent-Skills-Collection.git"
SKILLS_DIR="${HOME}/.agents/skills"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

print_banner() {
    echo ""
    echo -e "${CYAN}╔══════════════════════════════════════════════════╗${NC}"
    echo -e "${CYAN}║  ${BLUE}Ultimate Agent Skills Collection Installer${CYAN}      ║${NC}"
    echo -e "${CYAN}║  ${NC}49+ Production-Ready Skills for AI Agents${CYAN}        ║${NC}"
    echo -e "${CYAN}╚══════════════════════════════════════════════════╝${NC}"
    echo ""
}

log_info() { echo -e "${BLUE}[INFO]${NC} $1"; }
log_success() { echo -e "${GREEN}[OK]${NC} $1"; }
log_warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
log_error() { echo -e "${RED}[ERROR]${NC} $1"; }

declare -A IDE_PATHS
IDE_PATHS=(
    ["Cursor"]="${HOME}/.cursor/skills"
    ["Claude Code"]="${HOME}/.claude/skills"
    ["GitHub Copilot"]="${HOME}/.copilot/skills"
    ["Codex (OpenAI)"]="${HOME}/.codex/skills"
    ["Gemini CLI"]="${HOME}/.gemini/skills"
    ["Antigravity"]="${HOME}/.gemini/antigravity/skills"
    ["Windsurf"]="${HOME}/.codeium/windsurf/skills"
    ["OpenCode"]="${HOME}/.config/opencode/skill"
    ["Amp"]="${HOME}/.config/agents/skills"
    ["iFlow"]="${HOME}/.iflow/skills"
)

declare -A IDE_DETECTORS
IDE_DETECTORS=(
    ["Cursor"]="${HOME}/.cursor"
    ["Claude Code"]="${HOME}/.claude"
    ["GitHub Copilot"]="${HOME}/.copilot"
    ["Codex (OpenAI)"]="${HOME}/.codex"
    ["Gemini CLI"]="${HOME}/.gemini"
    ["Antigravity"]="${HOME}/.gemini/antigravity"
    ["Windsurf"]="${HOME}/.codeium/windsurf"
    ["OpenCode"]="${HOME}/.config/opencode"
    ["Amp"]="${HOME}/.config/agents"
    ["iFlow"]="${HOME}/.iflow"
)

detect_ides() {
    local detected=()
    for ide in "${!IDE_DETECTORS[@]}"; do
        if [ -d "${IDE_DETECTORS[$ide]}" ] || command -v "$(echo "$ide" | tr '[:upper:]' '[:lower:]' | tr -d ' ()')" &>/dev/null; then
            detected+=("$ide")
        fi
    done
    echo "${detected[@]}"
}

ensure_skills_source() {
    local script_dir
    script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

    if [ -f "${script_dir}/README.md" ] && [ -d "${script_dir}/docx" ]; then
        SKILLS_DIR="$script_dir"
        log_success "Using local skills from: ${SKILLS_DIR}"
        return 0
    fi

    if [ -d "${SKILLS_DIR}" ] && [ -f "${SKILLS_DIR}/README.md" ]; then
        log_success "Skills already available at: ${SKILLS_DIR}"
        return 0
    fi

    log_info "Cloning skills collection..."
    git clone --depth 1 "$REPO_URL" "$SKILLS_DIR"
    log_success "Skills cloned to: ${SKILLS_DIR}"
}

install_for_ide() {
    local ide="$1"
    local target="${IDE_PATHS[$ide]}"
    local parent_dir
    parent_dir="$(dirname "$target")"

    if [ -L "$target" ] && [ "$(readlink "$target")" = "$SKILLS_DIR" ]; then
        log_success "${ide}: Already configured"
        return 0
    fi

    if [ -e "$target" ]; then
        log_warn "${ide}: ${target} already exists, backing up to ${target}.bak"
        mv "$target" "${target}.bak"
    fi

    mkdir -p "$parent_dir"
    ln -sf "$SKILLS_DIR" "$target"
    log_success "${ide}: Linked ${target} -> ${SKILLS_DIR}"
}

mode_auto() {
    log_info "Auto-detecting installed IDEs..."
    local detected
    detected=$(detect_ides)

    if [ -z "$detected" ]; then
        log_warn "No IDEs detected. Installing for all supported IDEs..."
        mode_all
        return
    fi

    log_info "Detected IDEs: ${detected}"
    for ide in $detected; do
        install_for_ide "$ide"
    done
}

mode_all() {
    log_info "Installing for all supported IDEs..."
    for ide in "${!IDE_PATHS[@]}"; do
        install_for_ide "$ide"
    done
}

mode_select() {
    echo ""
    echo "Available IDEs:"
    echo ""

    local ide_list=()
    local i=1
    for ide in "${!IDE_PATHS[@]}"; do
        ide_list+=("$ide")
        local status=""
        if [ -L "${IDE_PATHS[$ide]}" ]; then
            status=" ${GREEN}(configured)${NC}"
        fi
        echo -e "  ${CYAN}${i})${NC} ${ide}${status}"
        ((i++))
    done

    echo ""
    echo -e "Enter numbers separated by spaces (e.g., ${CYAN}1 3 5${NC}), or ${CYAN}a${NC} for all:"
    read -r selection

    if [ "$selection" = "a" ]; then
        mode_all
        return
    fi

    for num in $selection; do
        local idx=$((num - 1))
        if [ $idx -ge 0 ] && [ $idx -lt ${#ide_list[@]} ]; then
            install_for_ide "${ide_list[$idx]}"
        else
            log_warn "Invalid selection: $num"
        fi
    done
}

print_summary() {
    echo ""
    echo -e "${GREEN}╔══════════════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║              Installation Complete!              ║${NC}"
    echo -e "${GREEN}╚══════════════════════════════════════════════════╝${NC}"
    echo ""
    echo "Configured IDEs:"
    for ide in "${!IDE_PATHS[@]}"; do
        local target="${IDE_PATHS[$ide]}"
        if [ -L "$target" ]; then
            echo -e "  ${GREEN}✓${NC} ${ide}: ${target}"
        fi
    done
    echo ""
    echo -e "Skills source: ${BLUE}${SKILLS_DIR}${NC}"
    echo -e "Total skills:  ${BLUE}49+${NC}"
    echo ""
    echo "Start using skills by opening your IDE and asking the AI agent!"
    echo ""
}

main() {
    print_banner

    ensure_skills_source

    echo ""
    echo "How would you like to install?"
    echo ""
    echo -e "  ${CYAN}1)${NC} Auto-detect    — Detect installed IDEs and configure them"
    echo -e "  ${CYAN}2)${NC} All IDEs       — Configure all supported IDEs"
    echo -e "  ${CYAN}3)${NC} Select IDEs    — Choose which IDEs to configure"
    echo ""
    read -rp "Choice [1/2/3]: " choice

    case "$choice" in
        1|"") mode_auto ;;
        2) mode_all ;;
        3) mode_select ;;
        *) log_error "Invalid choice"; exit 1 ;;
    esac

    print_summary
}

main "$@"
