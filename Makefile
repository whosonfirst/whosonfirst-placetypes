spec:
	python ./bin/compile.py > data/placetypes-spec-`date "+%Y%m%d"`.json
	cp data/placetypes-spec-`date "+%Y%m%d"`.json data/placetypes-spec-latest.json
