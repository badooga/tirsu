This package can be used to generate an SVG file of [Tir'su](https://forgottenrealms.fandom.com/wiki/Gith_language) glyphs from Latin characters. For more information on the Tir'su language, see [this](https://archiveofourown.org/works/52500334) resource.

### Usage
For basic usage, simply run `python tirsu/main.py` and supply the requested inputs. If you use this from within a Python script, you can instead use `from tirsu import write_tirsu`.

Note that while commas are ignored, a period, question mark, or exclamation point will indicate a line break. Other characters, such as numbers, will raise an error.

### Examples
Below are examples of Tir'su glyphs generated with this tool.

Ch'mar, zal'a Vlaakith (Vlaakith's will above all), githyanki style

<img src="examples/zala.svg" alt="Tir'su glyphs for the githyanki phrase Ch'mar, zal'a Vlaakith" >

Rrakkma (illithid hunting party), githzerai style

<img src="examples/rrakkma.svg" alt="Tir'su glyphs for the githzerai word rrakkma" >

Ch'mar, zal'a Orpheus! Mha stil'na forjun inyeri! (Orpheus' will above all! May the Comet blaze my path forward!), githyanki style

<img src="examples/orpheus.svg" alt="Tir'su glyphs for the githyanki phrase Ch'mar, zal'a Orpheus! Mha stil'na forjun inyeri!" >

### Credits
I used the resources in the [Tirsu-Writer](https://github.com/Landhund/TirSu-Writer) project to make this project; the included measurements of each letter's lengths and angles were what made all of this possible in the first place.
