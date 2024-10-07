# TranscriptAnalyzer

Compare the transcripts of two or more youtube videos and determine if the creators are having converstaions availablein both videos.

## Setup

1. Clone the repository:

```bash
git clone https://github.com/cgallarno/TranscriptAnalyzer.git
cd TranscriptAnalyzer
```

2. Create / activate virtual envrionment

```
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Use it!
   - Videos in common:

```bash
python3 main.py VeH1fynKu6w 6KxT-yGbvBo
```


Spycakes and TFG
```bash
python3 main.py VPZlLr3hkd4 gam8OM_7Wn8
```

    * Videos NOT in common:

```bash
python3 main.py VeH1fynKu6w 5pUCF6RQa50
```
