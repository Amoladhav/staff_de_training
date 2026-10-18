# Source from Bash. Project-maintained completion for common dbt v2 commands
# and options; no model-name completion or database calls. Not a dbt generator.
_staff_de_dbt_completion() {
    local current="${COMP_WORDS[COMP_CWORD]}"
    local candidates
    COMPREPLY=()
    if (( COMP_CWORD == 1 )); then
        candidates='init deps parse list ls compile check run run-operation test seed snapshot show build clean source freshness clone man debug retry docs login state system format lint license sl wizard help'
    elif [[ "$current" == -* ]]; then
        candidates='--help --select --exclude --selector --target --project-dir --profiles-dir --target-path --log-path --threads --vars --no-version-check --no-manage-state --no-send-anonymous-usage-stats'
    elif (( COMP_CWORD == 2 )) && [[ "${COMP_WORDS[1]}" == source ]]; then
        candidates='freshness'
    elif (( COMP_CWORD == 2 )) && [[ "${COMP_WORDS[1]}" == docs ]]; then
        candidates='generate serve'
    else
        return 0
    fi
    mapfile -t COMPREPLY < <(compgen -W "$candidates" -- "$current")
}
complete -o default -F _staff_de_dbt_completion dbt
