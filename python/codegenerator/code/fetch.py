def loadRelation(path,name,annotationType,memType):
 	code = """
    Trie<%(annotationType)s,%(memType)s> *Trie_%(name)s = NULL;
    {
      auto start_time = timer::start_clock();
      // loadTrie
      Trie_%(name)s = Trie<%(annotationType)s,%(memType)s>::load("%(path)s");
      timer::stop_clock("LOADING TRIE %(name)s", start_time);
    }"""% locals()
	return code

def loadEncoding(path,name,type):
	code = """
	Encoding<long> *Encoding_%(name)s = NULL;
	{
    auto start_time = timer::start_clock();
    Encoding_%(name)s = Encoding<%(type)s>::from_binary(
        "%(path)s/encodings/node/");
    timer::stop_clock("LOADING ENCODINGS %(name)s", start_time);
    }
	"""% locals()
	return code

def setResult(name,encodings):
	code = """encodings = new std::vector<void*>();"""
	for e in encodings:
		code += """encodings->push_back((void*)Encoding_%(e)s);"""% locals()
	code+="""result = (void*)Trie_%(name)s;"""% locals()
	return code