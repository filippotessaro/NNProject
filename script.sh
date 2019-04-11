for num in {01..24}; do
  mkdir export/Actor_$num
done
find Audio_Speech_Actors_01-24/ -type f -iname "*.wav" -exec sh -c \
'bn=${1#*/} bn=${bn%.*}; ffmpeg -loglevel 16 -i "$1" "${0}${bn}.wav"' export/ {} \;
