//defines a single neuron object

#ifndef EVALNET_WEIGHT_H
#define EVALNET_WEIGHT_H

namespace evn {

	class Neuron;

	class Weight {

		Neuron* prev;
		Neuron* next;

		double weight_value; //magnitude of this weight
		double last_input;

	public:

	};

}

#endif
