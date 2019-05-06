import argparse


def get_args():
    parser = argparse.ArgumentParser()

    #data
    parser.add_argument('--train_file',type=str,default=None,help="trainning file")
    parser.add_argument('--dev_file',type=str,default=None,help="development file")

    #model
    parser.add_argument('--batch_size', type=int, default=32, help="batch size for trainning")
    parser.add_argument('--num_epochs', type=int, default=10, help="number of epoch for trainning")
    parser.add_argument('--learning_rate', type=float, default=0.001, help="learning rate of Adam")
    parser.add_argument('--embedding_size', type=int, default=256, help="embedding size")

    return parser.parse_args()