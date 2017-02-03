FROM elasticsearch:1.7

RUN plugin install mobz/elasticsearch-head
RUN plugin install elasticsearch/elasticsearch-cloud-aws/2.7.1

EXPOSE 9200 9300

CMD ["elasticsearch"]
