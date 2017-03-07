NAME=camera_web

docker build -t $NAME .

docker rm $NAME 
docker run -ti \
    -v $(pwd):/web \
    -e FLASK_DEBUG=1 \
    --name=$NAME -p 5000:5000 $NAME

        
