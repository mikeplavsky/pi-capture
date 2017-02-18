BUCKET=$1

DATE=$(date +"%Y-%m-%d_%H_%M")
BASEDIR=$(dirname "$0")

rm $BASEDIR/*.jpg

FILE=$BASEDIR/$DATE.jpg

fswebcam --fps 15 -S 8 -r 640x480  $FILE
aws s3 cp $FILE s3://$BUCKET

