from abc import ABC

from alr_sim.core.sim_object.sim_object import SimObject
from alr_sim.sims.mujoco.MujocoLoadable import MujocoXmlLoadable


class Hammer(SimObject, MujocoXmlLoadable, ABC):

    def __init__(self, name: str, init_pos, init_quat):
        super(Hammer, self).__init__(name, init_pos, init_quat)
        self.xml_file_path = "/home/jan/SimulationFramework/models/mujoco/objects/assets/hammer_dependencies.xml"

    def xml_file_path(self):
        return self.xml_file_path

    def get_poi(self) -> list:
        return [self.name]