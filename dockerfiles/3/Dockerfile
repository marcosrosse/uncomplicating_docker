FROM golang AS building

WORKDIR /app
ADD . /app
RUN go build -o utopia


FROM alpine
WORKDIR realidade
COPY --from=building /app/utopia /realidade
ENTRYPOINT ./utopia 
