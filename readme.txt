How to run:
    For train mode (Data preprocess -> Building a Decision Tree -> Test Decision Tree in Test set ):
        python main.py --model_mode train --training_set data/adult.data  --testing_set data/adult.test --max_layer 15

    For test mode (Just test Decision Tree in Test set ):
        python main.py --model_mode test --processed_testing_set data/adult.clean_test --tree tree.txt

    The input parameters and their meanings:
        --model_mode:      type=str, default="train", help='Model mode: training mode or testing mode'
        --training_set:    type=str, default="data/adult.data", help='Input training set file'
        --testing_set':    type=str, default="data/adult.test", help='Input testing set file'
        --processed_testing_set':type=str, default="data/adult.clean_test",help='Input preprocessed testing set file'
        --tree:            type=str, default="tree.txt", help='The input decision tree model file'
        --max_layer:       type=int, default=14, help='Max Number of decision tree layers'

    About the running Time:
        We run this program in Macbook with M2 Max chip, and when the depth is 15, the required time is 362 seconds.
        This time is just for your reference, for detail please see our project report.

        If you think the decision tree generation time is too long, please directly use the test mode to evaluate our model.
        The trained decision tree model is saved in the tree.txt file.


After running, the program will generate the following files:
    data/adult.clean_data:     preprocessed training data
    data/adult.clean_test:     preprocessed testing data
    tree.txt:             decision tree model data
    correct_classify.txt: contains all the correct classified records in testing set
    mis_classify.txt:     contains all the mis classified records in testing set




