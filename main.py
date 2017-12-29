import Repository
import RawMaterial


tmp_re = Repository.Repository(2, 2)
tmp_rm = RawMaterial.RawMaterial(2, 2)
tmp_re.append_raw_material(tmp_rm)
print(tmp_re.get_utilized_raw_material_capacity())