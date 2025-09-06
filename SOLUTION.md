Modified the Mapper.py file to count urls instead of words by using regular expressions, `href="([^"]*)"` to capture the urls in the hrefs from the html files.

Modified the Reducer.py file to count only output only the urls that have counts > 5.

Final url counts are as follows:

```
#	20
/wiki/Doi_(identifier)	18
/wiki/Google_File_System	6
/wiki/ISBN_(identifier)	18
/wiki/MapReduce	7
/wiki/S2CID_(identifier)	14
mw-data:TemplateStyles:r1129693374	7
mw-data:TemplateStyles:r1238218222	121
mw-data:TemplateStyles:r1295599781	33
mw-data:TemplateStyles:r886049734	12

```

Ran the code on the distributed Hadoop cluster using dataproc, and had the following results.

#### Running with 2 workers

Times:

- real: 1m30.802s
- user: 0m15.667s
- sys: 0m1.286s

#### Running with 4 workers

Times:

- real: 1m10.566s
- user: 0m15.455s
- sys: 0m1.128s

Based on the above timings, it seems like there is minimal improvement in speed in proportion to the increase in workers. The user time which represents the actual CPU time spent on the code is almost identical indicating that there is some bottleneck that can't be solved by just increasing the number of workers.
