from __future__ import print_function

import dataset
import explore_utils
import argparse


def main(args):

    print("Loading the dataset...")
    data = dataset.Dataset(args.debug)

    print("Number of rows in the training set:    ", len(data.train))
    print("Number of columns in the training set: ", len(data.train.columns))

    print("Number of rows in the test set:        ", len(data.test))
    print("Number of columns in the test set:     ", len(data.test.columns))

    # Number of visits

    print("The most visit times for a customer in train set is: ",
          explore_utils.find_most_visit(data))

    # Customer spending percentiles

    percentiles = [95, 97.5, 99, 99.9, 99.99]
    percentile_values = explore_utils.find_customer_revenue_percentiles(
        data,
        percentiles)
    for p, pv in zip(percentiles, percentile_values):
        print("%2.2f%% of customers spend less than: $%.2f" % (p, pv))

    # Most common Sources of Traffic and counts
    num_of_sources = 6
    most_common_sources = explore_utils.find_most_common_traffic_sources(data, num_of_sources)
    print("\nThe {} most common sources of traffic are :".format(num_of_sources))
    for source in most_common_sources.index:
        print(' {}: {}'.format(source, most_common_sources[source]))

    # channelGroupings and customer revenue (#31)
    counts, means = explore_utils.find_channel_grouping_revenue(data)
    print('Channel Grouping Counts:')
    for key in sorted(counts, key=counts.get, reverse=True):
        print('\t{}: {}'.format(key, counts[key]))

    print('Mean Total Revenue by Channel Grouping')
    for key in sorted(means, key=means.get, reverse=True):
        print('\t{}: ${:.2f}'.format(key, means[key]))

    # transactionRevenue by region

    trans_by_region = explore_utils.find_transaction_by_region(data)
    print("The transaction revenues by region are: ", trans_by_region)


    # Unique Visitor Percentage
    print("%2.2f%% of all visitors to the site visit exactly once." % explore_utils.find_one_visit_percent(data))

    # Summary statistics for revenue generated, by device
    # First print-out includes sessions that didn't produce revenue
    # Second print-out only includes sessions that generated revenue
    print("Revenue summary statistics by device, zeroes included: \n",
          explore_utils.find_revenue_summary_statistics_for_devices(data, True))
    print ("Revenue summary statistics by device, zeroes excluded: \n",
           explore_utils.find_revenue_summary_statistics_for_devices(data, False))

    # Prints out what percent of revenue generating sessions were accessed via a particular device
    print("Percent of revenue generating sessions that used a particular device: \n",
          explore_utils.find_percent_sessionIds_using_certain_device(data))

    # Prints out the percent of total revenue that can be attributed to sessions
    # accessed via a particular device
    print("Percent of total revenue attributed to sessions using a particular device: \n",
          explore_utils.find_percent_of_total_revenue_by_device(data))

    # Prints out the percent of sessions accessed via a particular device taht
    # generated revenue
    print("Percent of total sessions using a particular device that generated revenue: \n",
          explore_utils.find_percent_device_uses_generating_revenue(data))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Explore the Google Analytics dataset.')
    parser.add_argument('--debug', dest='debug', action='store_true',
                        help='run in debug mode')
    args = parser.parse_args()

    main(args)
