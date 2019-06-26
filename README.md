# Email Spam Classifier

This program aims to classify emails as spam or non-spam(ham) by creating and using a custom dataset derived by going through your very own email boxes.

Read mails from the inboxes of the accounts we intend to read using the imap server, we then create a dictionary of words based on the common words that are used in Spam mails and non-spam mails.

Formation of a  frequency table of the number of words in each mail and create a labelled dataset of classifying the particular word as spam or non spam.

Created a 70-30 split on training to test data from our dataset of words.

Train Naive-Bayes model based on this dataset. 

Tested data yielded an accuracy score of 93%

The major learning outcome of this project was that i learnt to play around with Python's nltk library , sci-kit , pandas and Machine learning models.

