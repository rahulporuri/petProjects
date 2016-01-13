#echo "$@.tar.gz"
for dir in /media/rahulporuri/data/palladium/cubed/{.,}*; do
#	echo "$dir.tar.gz" "$dir"
	tar czvf "$dir.tar.gz" "$dir"
done
