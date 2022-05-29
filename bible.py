import os, re, sqlite3

class Bible:
    def __init__(self, version: str):
        self._version = version.lower()
        self.db_path = 'data/' + self._version + '.sqlite3'

        if not os.path.isfile(self.db_path):
            raise FileNotFoundError("[Bible] Unsupported version: " + version)

        self.con = sqlite3.connect(self.db_path)
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()

    @property
    def version(self) -> str:
        return self._version.upper()

    def get_books(self) -> list[sqlite3.Row]:
        return self.cur.execute('select * from book')

    def find_book_by_name(self, name: str) -> sqlite3.Row:
        alternative = name.replace(' ', '')
        sql = "select * from book where lower(name) like lower(?) or lower(name) like lower(?) limit 1"
        result = self.cur.execute(sql, (name, alternative)).fetchone()
        
        return result

    def get_verses(self, book: int, chapter: int, verse_start: int, verse_end: int) -> list[sqlite3.Row]:
        sql = "select * from verse where book_id = ? and chapter = ? and verse >= ? and verse <= ?"
        stmt = self.cur.execute(sql, (
            book,
            chapter,
            verse_start,
            verse_end))

        return stmt.fetchall()

    def get_verses_by_string(self, context: str) -> list[sqlite3.Row]:
        regex = re.compile(r'((?:\d\s)?\w+)\s?(\d+)(?::|\.)?(\d+)?(?:-)?(\d+)?')
        result = regex.match(context)

        if not result:
            raise Exception("[Bible] Unregonized context format: " + context)
        
        input_book_name = result.group(1)
        input_chapter = result.group(2)
        input_verse_start = result.group(3)
        input_verse_end = result.group(4) or input_verse_start
        book = self.find_book_by_name(input_book_name)

        if not book:
            raise Exception("[Bible] Book not found: " + input_book_name)

        # print("Input: %s \nBook: %s \nChapter: %s \nVerse Start: %s \nVerse End: %s" % (
        #     context,
        #     input_book_name,
        #     input_chapter,
        #     input_verse_start,
        #     input_verse_end,))

        if not input_verse_start:
            input_verse_start = 1
            input_verse_end = 999

        return self.get_verses(
            int(book['id']),
            int(input_chapter),
            int(input_verse_start),
            int(input_verse_end))
