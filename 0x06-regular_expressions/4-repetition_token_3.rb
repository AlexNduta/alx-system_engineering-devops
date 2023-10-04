#!/usr/bin/env ruby
#matches hbn, hbtn, hbttn, hbtttn, hbttttn
puts ARGV[0].scan(/hbt*n/).join
