set -e   
echo Building...👷
echo $*

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
      out="build/$name.html"
      title="$(fixTitle $name)"

      echo "$f -> $out"
      pandoc -s $f -t dzslides -o "$out"\
         --self-contained\
         --template "template/my.dzslides"\
         --metadata title="$title"\
         --metadata date="$(date --iso-8601)"\
         --metadata author="Peder G. Landsverk"
   done
echo Done!🎉
