FROM cloudacademydevops/ide:python-3.8.3
USER root
WORKDIR /root/lab/
COPY src ./src
COPY test ./test
CMD [ "-f", "/dev/null" ]
ENTRYPOINT [ "tail" ]