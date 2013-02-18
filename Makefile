run:
	python spacedHexEncoder.py
	python spacedHexDecoder.py

clean:
	rm output
	rm hash

encode:
	python spacedHexEncoder.py

decode:
	python spacedHexDecoder.py
