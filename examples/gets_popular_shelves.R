library(dplyr)

books <- read.csv(file='ff-books.csv', sep = ',', stringsAsFactors = F, header = T)

test <- books %>%
  group_by(shelve) %>% 
  count(shelve) %>%
  arrange(desc(n))

test2 <- test %>%
  filter(n > 50)

getSilimlars <- function(data, str){
  data <- data  %>%
    filter(grepl(str, shelve))
  return(data)
}

test2 <- test2 %>%
  filter(!grepl('read|lgbt|ff|f-f|glbt|other|want|own|ya|recom|list|buy|kindle|maybe|default|gay|reviewed|queer|borrowed|finish|have|wlw|dnf|my-library|nonfiction|gblt|not-for-me|female-protagonist|lr|tbr|verified|library|love|fem|gender-and-sexuality|to-get|usa|women|young-adult-fiction|standalone|teen|scifi|sci-|quiltbag|novel|library|not-interested|mystery-thriller|memoirs|literary|les|historical-fiction|history|general-fiction|favourites|english|contemporary-fiction|chick-lit|abandoned|all-time-favorites|audible|arc|bold-strokes|e-book|epub|0s|gender|faves|sex|calibre|america|word|bella|best|main|mystery-|paranormal-|romance-|shel|thriller-', shelve)) %>%
  filter(!shelve %in% c("a", "audio", "audio-books", "audiobooks", "book-club", "books", "ebooks", "l", "l-books", "funny", "my-books", "mysteries", "signed", "gender", "favorite", "adult-fiction", "04-stars", "03-stars", "ebooks-kobo", "high-school", "literature","romance", "netgalley", "100", "4-rating","angst","anthologies","audio-book","next","general","graphics","speculative-fiction","erotic","q","poc","comic","sf","oh-hold","bookclub","favourite","nook","not-now","favorite-authors","graphic","need","contemporary-romance","comic-books","biographies","biography-memoir", "british", "canadian", "comix", "dystopia", "england", "essays", "first-in-series", "for-the-girls","gave-up-on", "giveaways", "good", "high-fantasy", "humour", "lbgtq", "lez-be-honest","lg","lg-books","memoir-biography","mental-health","mental-illness","mine","science-fiction-fantasy","series-all","shifters","vampire","youngadult","soulmates","sequential-art","sapphic","race","old","norm-cops-n-robbers","non-fic","nookbooks","ni","new-adult","lendable","my-fake-life","on-hold","paperback","mundane", "toaster-oven"))

shelves <- test2$shelve
