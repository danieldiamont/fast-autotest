find -type f -name '*.py' ! -path '*/.env/*' -exec autopep8 --in-place --aggressive --aggressive '{}' \;
