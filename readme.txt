How to run:
    For train mode
        python main.py --model_mode train --training_set data/adult.data  --testing_set data/adult.test --max_layer 14
    For test mode
        python main.py --model_mode test --processed_testing_set data/adult.clean_test --tree tree.txt

    The input parameters and their meanings
        --model_mode:      type=str, default="train", help='Model mode: training mode or testing mode'
        --training_set:    type=str, default="data/adult.data", help='Input training set file'
        --testing_set':    type=str, default="data/adult.test", help='Input testing set file'
        --processed_testing_set':type=str, default="data/adult.clean_test",help='Input preprocessed testing set file'
        --tree:            type=str, default="tree.txt", help='The input decision tree model file'
        --max_layer:       type=int, default=14, help='Max Number of decision tree layers'

After running, the program will generate the following files:
    data/adult.clean_data:     preprocessed training data
    data/adult.clean_test:     preprocessed testing data
    tree.txt:             decision tree model data
    correct_classify.txt: contains all the correct classified records in testing set
    mis_classify.txt:     contains all the mis classified records in testing set


