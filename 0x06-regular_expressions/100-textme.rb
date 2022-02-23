#!/usr/bin/env ruby
fields = ARGV[0].scan(/\[((from|to|flags):([^\]]+))\]/)
fields = fields.map { |arr|  arr[2] }
puts "#{fields[0]},#{fields[1]},#{fields[2]}"
