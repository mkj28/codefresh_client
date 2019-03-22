SOURCE ?= https://g.codefresh.io/api/openapi.json

.PHONY: generate
generate:
	openapi-generator generate -i $(SOURCE) -g python -o . --skip-validate-spec --additional-properties packageName=codefresh_client --additional-properties packageVersion=0.0.2 --additional-properties packageUrl=https://g.codefresh.io/api/openapi.json

.PHONY: fetch
fetch:
	wget -q $(SOURCE) -O codefresh_openapi.json
