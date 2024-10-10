import { motion } from 'framer-motion';
import Mask from './Mask';

export default function MaskBox({ children, duration = 0.5, delay = 0, color = '#000', style }) {
	//styles
	const frameStyle = {
		display: 'inline-block',
		position: 'relative',
		overflow: 'hidden'
	};

	//motion options
	const motionBox = {
		in: { opacity: 0 },
		on: { opacity: 1 },
		out: { opacity: 0, transition: { delay: 0 } },
		time: { duration: 0.01, delay: duration / 2 + delay }
	};

	return (
		<div style={{ ...frameStyle, ...style }}>
			<motion.div
				style={{ width: '100%', height: '100%' }}
				variants={motionBox}
				initial='in'
				animate='on'
				exit='out'
				transition={motionBox.time}>
				{children}
			</motion.div>

			<Mask duration={duration} delay={delay} color={color} />
		</div>
	);
}
