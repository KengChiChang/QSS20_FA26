# count_whilst.sh: the same question, as shell commands
echo "Essays that contain 'whilst':"
grep -il 'whilst' data/raw/federalist/fp*.txt | wc -l
echo "Essays that contain 'while':"
grep -il 'while' data/raw/federalist/fp*.txt | wc -l
