FROM debian:stable-slim
# COPY source destination
COPY Asteroids /bin/Asteroids
ENV PORT=8080
CMD [ "/bin/Asteroids" ]