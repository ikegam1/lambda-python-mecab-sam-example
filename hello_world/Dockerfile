FROM public.ecr.aws/lambda/python:3.9

RUN yum install -y file tar gzip unzip gcc make swig gcc-c++ git

RUN curl -L 'https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7cENtOXlicTFaRUE' -o mecab-0.996.tar.gz \
    && tar zvxf mecab-0.996.tar.gz
RUN (cd mecab-0.996 && ./configure --prefix=/var/task --enable-utf8-only && make && make install)
RUN curl -L "https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7MWVlSDBCSXZMTXM" -o mecab-ipadic-2.7.0-20070801.tar.gz \
    && tar -zxvf mecab-ipadic-2.7.0-20070801.tar.gz
RUN (cd mecab-ipadic-2.7.0-20070801 \
    && ./configure --prefix=/var/task --with-charset=utf8 --with-mecab-config=/var/task/bin/mecab-config && make && make install)
RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
RUN yum install -y which xz patch openssl
RUN ln -s /var/task/bin/* /var/lang/bin/
RUN (cd mecab-ipadic-neologd && ./bin/install-mecab-ipadic-neologd -n -a -y)

COPY app.py requirements.txt ./
RUN python3.9 -m pip install -r requirements.txt -t .

# Command can be overwritten by providing a different command in the template directly.
CMD ["app.lambda_handler"]
