set -e   
echo Building...👷

makeHeader() 
{
   echo "% $*\n% Peder G. Landsverk\n% $(date --iso-8601)
   "
}

titleCase()
{
   echo $1 | sed 's/.*/\L&/; s/[a-z]*/\u&/g'
}

fixTitle()
{
   echo "$(titleCase $*)" | sed 's/_/ /g'
}

for f in src/*
   do
      name="$(echo $f | cut -f 2 -d '/' | cut -f 1 -d '.')"
      out="build/$name.htm"
      title="$(fixTitle $name)"

      echo "$f -> $out"
      echo "$(makeHeader $title)" | cat - $f |\
         pandoc -t dzslides -o "$out" \
         --self-contained \
         --template "template/my.dzslides"
   done
echo Done!🎉
