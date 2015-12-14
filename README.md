## Dstat MongoDB plugins

- MongoDB operations counter (<strong>--mongodb-opcount</strong>), counting  queries, inserts, updates, deletes, getmores and commands.</li>
- MongoDB data size statistics (<strong>--mongodb-stats</strong>), displaying ddata size, the index size and the actual size.</li>
- MongoDB connection  counter (<strong>--mongodb-conn</strong>), number of used and available connections</li>
- MongoDB memory information (<strong>--mongodb-mem</strong>), resident and virtual memory. Journal memory and page faults are added if  MMAPV1 is used.</li>
- MongoDB monitoring (<strong>--mongodb</strong>), gathering all previous metrics

**Example:**
<pre class="lang:default decode:true">./dstat --mongodb
 -----------mongodb-counts---------- --mongodb-stats-- mongodb-con mongodb-mem
| qry   ins   upd   del   gtm   cmd |dsize isize ssize| curr avail| res   virt
|    0     0     0     0     0     0|  855   424   381|    8   811| 1766  2133
|    0     0     0     0     0     7|  855   424   381|    8   811| 1766  2133
|    0     0     0     0     0     5|  855   424   381|    8   811| 1766  2133
</pre>

**Usefull environment variables:**
- _DSTAT_MONGODB_USER_, if specifified, the provided username will be used for authentication
- _DSTAT_MONGODB_PWD_, if specified, this password will be used for authentication
- _DSTAT_MONGODB_HOST_, default value is _127.0.0.1:27017_, must be change if mongo is listening on a different port.

For more information, please see: [Monitoring MongoDB with Dstat](http://lamada.eu/blog/2015/08/27/monitoring-mongodb-with-dstat/)

## Dstat

Dstat is a versatile replacement for vmstat, iostat, mpstat, netstat and
ifstat. Dstat overcomes some of their limitations and adds some extra
features, more counters and flexibility. Dstat is handy for monitoring
systems during performance tuning tests, benchmarks or troubleshooting.

Dstat allows you to view all of your system resources instantly, you
can eg. compare disk usage in combination with interrupts from your
IDE controller, or compare the network bandwidth numbers directly
with the disk throughput (in the same interval).

Dstat gives you detailed selective information in columns and clearly
indicates in what magnitude and unit the output is displayed. Less
confusion, less mistakes.

Dstat is unique in letting you aggregate block device throughput for
a certain diskset or networkset, ie. you can see the throughput for
all the block devices that make up a single filesystem or storage
system.

You can write your own dstat plugins to monitor whatever you like in
just a few minutes based on provided examples and a little bit of
Python knowledge.

Dstat's output by default is designed for being interpreted by humans
in real-time, however the new CSV output allows you to store CSV
output in detail to a file to be imported later into LibreOffice or Excel
to generate graphs.

Since it's practically impossible to test dstat on every possible
permutation of kernel , python or distribution version, I need your
help and your feedback to fix the remaining problems.

If you have improvements or bugreports, please send them to:

    http://github.com/dagwieers/dstat
