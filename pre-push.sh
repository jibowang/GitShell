
#!/bin/bash
# Prevents force-pushing to master.
# Based on: https://gist.github.com/pixelhandler/5718585
# Install:
# cd path/to/git/repo
# curl -fL -o .git/hooks/pre-push https://gist.githubusercontent.com/stefansundin/d465f1e331fc5c632088/raw/pre-push
# chmod +x .git/hooks/pre-push


BRANCH=`git rev-parse --abbrev-ref HEAD`
PUSH_COMMAND=`ps -ocommand= -p $PPID`
PROTECTED_BRANCHS=("master" "rc" "dev")

if [[ "${PROTECTED_BRANCHS[@]}" =~ "$BRANCH" && "$PUSH_COMMAND" =~ force|delete|-f ]]; then
  echo
  echo "Prevented force-push to $BRANCH. This is a very dangerous command."
  echo "If you really want to do this, use --no-verify to bypass this pre-push hook."
  echo
  exit 1
fi

exit 0
