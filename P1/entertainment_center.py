import media
import fresh_tomatoes

# Create 3 instances of the Movie() class

imitation_game = media.Movie("Imitation Game",
                             "The Imitation Game is a 2014 historical thriller "
                             "film directed by Morten Tyldum, with a screenplay "
                             "by Graham Moore loosely based on the biography "
                             "Alan Turing: The Enigma by Andrew Hodges. It stars "
                             "Benedict Cumberbatch as the British cryptanalyst "
                             "Alan Turing, who helped solve the Enigma code during "
                             "the Second World War and was later prosecuted for "
                             "homosexuality.",
                             "http://www.riverviewtheater.com/system/assets/0000"
                             "/2283/The-Imitation-Game-poster-1.jpg?1421211491",
                             "https://www.youtube.com/watch?v=S5CjKEFb-sM")

the_theory_of_everything = media.Movie("The Theory Of Everything",
                                       "The Theory of Everything is a 2014 "
                                       "British biographical coming of age "
                                       "romantic drama film[4] directed by "
                                       "James Marsh and adapted by Anthony "
                                       "McCarten from the memoir Travelling "
                                       "to Infinity: My Life with Stephen by "
                                       "Jane Wilde Hawking, which deals with "
                                       "her relationship with her former "
                                       "husband, theoretical physicist Stephen "
                                       "Hawking, his diagnosis of motor neuron "
                                       "disease, and his success in physics.",
                                       "http://www.cvfilms.org/wp-content/uploads"
                                       "/2015/02/Theory-of-Everything-studio-1.jpg",
                                       "https://www.youtube.com/watch?v"
                                       "=Salz7uGp72c")

american_sniper = media.Movie("American Sniper",
                              "American Sniper is a 2014 American biographical "
                              "war drama film[6] directed by Clint Eastwood and "
                              "written by Jason Hall. It is based on the book "
                              "American Sniper: The Autobiography of the Most "
                              "Lethal Sniper in U.S. Military History (2012) by "
                              "Chris Kyle, with Scott McEwen and Jim DeFelice. "
                              "The film follows the life of Kyle, who became the "
                              "deadliest marksman in U.S. military history with "
                              "255 kills from four tours in the Iraq War, 160 of "
                              "which were officially confirmed by the Department "
                              "of Defense.",
                              "http://ogpdn1wn2d93vut8u40tokx1dl7.wpengine.netdna"
                              "-cdn.com/wp-content/uploads/2015/01/thumbRNS-"
                              "AMERICAN-SNIPER011315c.jpg",
                              "https://www.youtube.com/watch?v=99k3u9ay1gs")

# Populate them into a list and pass into the open_movies_page API

movies = [imitation_game, the_theory_of_everything, american_sniper]
fresh_tomatoes.open_movies_page(movies);
